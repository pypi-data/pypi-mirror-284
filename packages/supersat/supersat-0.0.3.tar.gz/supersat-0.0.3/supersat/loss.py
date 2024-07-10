import torch
import lpips

from abc import ABC, abstractmethod

# Create a template for the loss functions
class super_loss(ABC, torch.nn.Module):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def forward(
        self, lr: torch.Tensor, sr: torch.Tensor, hr: torch.Tensor
    ) -> torch.Tensor:
        pass



class l1_loss(super_loss):
    def __init__(self):
        super().__init__()

    def forward(self, lr, sr, hr):
        return torch.mean(torch.abs(sr - hr))
    

class lpips_loss(torch.nn.Module):
    def __init__(
        self,
        to_true_color: bool = True,        
        rgb_bands: list = [0, 1, 2]
    ):
        super().__init__()
        self.loss_fn_alex = lpips.LPIPS(net='alex')
        self.to_true_color = to_true_color
        self.rgb_bands = rgb_bands

    def forward(self, lr, sr, hr):
        
        # Normalize the images to the range [0, 1]
        if self.to_true_color:
            sr = torch.clamp(sr * 3, 0, 1)
            hr = torch.clamp(hr * 3, 0, 1)
        
        # Normalize the images to the range [-1, 1]
        sr_1 = sr[self.rgb_bands] * 2 - 1
        hr_1 = hr[self.rgb_bands] * 2 - 1
        
        return self.loss_fn_alex(sr_1, hr_1).mean()


class opensrtest_loss(torch.nn.Module):
    def __init__(
        self,
        gradient_threshold: float = 0.50,
        regularization_parameter: float = 0.05,
        softmin_temperature: float = 0.25,
        return_map: bool = False
    ):
        """ The opensrtest loss function

        Args:
            gradient_threshold (float, optional): The threshold
                value for the gradient. Defaults to 0.75.
            regularization_parameter (float, optional): The 
                regularization parameter. Defaults to 0.05.
            softmin_temperature (float, optional): The temperature
                for the softmin function. Defaults to 0.25.
            return_map (bool, optional): If the function should
                return the map. Defaults to False.
        """
        super().__init__()
        self.gradient_threshold = gradient_threshold
        self.regularization_parameter = regularization_parameter
        self.softmin_temperature = softmin_temperature
        self.return_map = return_map
    
    def normalized_difference(self, x: torch.Tensor, y: torch.Tensor) -> torch.Tensor:
        """ By default, the function calculates the normalized
        difference between two tensors along the channel
        dimension. The function is defined as:        

        Args:
            x (torch.Tensor): The first tensor.
            y (torch.Tensor): The second tensor.

        Returns:
            torch.Tensor: The normalized difference between the
                two tensors.
        """
        return torch.mean(torch.abs(x - y) / (x + y), dim=1)

    def forward(
        self,
        lr: torch.Tensor,
        sr: torch.Tensor,
        hr: torch.Tensor
    ) -> torch.Tensor:
        """ The forward function calculates the opensrtest
        loss function. The function is defined as:                

        Args:
            lr (torch.Tensor): The low-resolution image.
            sr (torch.Tensor): The super-resolved image.
            hr (torch.Tensor): The high-resolution image.

        Returns:
            torch.Tensor: The opensrtest loss.
        """


        # Align the histograms of the SR and HR images
        #hr = hq_histogram_matching(hr, sr)
        
        # Generate a reference LR image
        lr_hat = torch.nn.functional.interpolate(
            input=lr,
            size=hr.shape[-2:],
            mode='bilinear',
            antialias=True
        )
        
        # Obtain the three distance metrics
        d_ref = self.normalized_difference(lr_hat, hr)
        d_om = self.normalized_difference(lr_hat, sr)
        d_im = self.normalized_difference(sr, hr)
        
        # Create a mask to filter out the gradients
        # with a magnitude below the threshold value
        gradient_threshold = d_ref.flatten().kthvalue(
                int(self.gradient_threshold * d_ref.numel())
        ).values.item()

        mask1 = (d_ref > gradient_threshold) * 1.
        mask2 = (d_im > gradient_threshold) * 1.
        mask3 = (d_om > gradient_threshold) * 1.
        mask = ((mask1 + mask2 + mask3) > 0) * 1.
        
        # Calculate the improvement based on the masks
        if self.return_map:
            mask[mask == 0] = torch.nan
            d_ref = d_ref * mask
            d_im =  d_im * mask
            d_om =  d_om * mask

            # Compute relative distance
            d_im_ref = d_im / d_ref
            d_om_ref = d_om / d_ref            
        else:            
            # Estimate the masked distances 
            d_im_masked = torch.masked_select(d_im, mask.bool())
            d_om_masked = torch.masked_select(d_om, mask.bool())
            d_ref_masked = torch.masked_select(d_ref, mask.bool())
            d_im_ref = d_im_masked / d_ref_masked
            d_om_ref = d_om_masked / d_ref_masked
        
        # Estimate the scores
        H = d_im_ref + d_om_ref -1
        im_score = d_im_ref + d_om_ref*(1 - torch.exp(-H*self.regularization_parameter))
        om_score = d_om_ref + d_im_ref*(1 - torch.exp(-H*self.regularization_parameter))
        ha_score = torch.exp(-d_im_ref * d_om_ref * self.regularization_parameter)

        # Calculate the sofmin
        score_stack = torch.stack([im_score, om_score, ha_score], dim=1)
        exp_neg_x_over_T = torch.exp(-score_stack / self.softmin_temperature)
        score_stack = exp_neg_x_over_T / exp_neg_x_over_T.sum(dim=1, keepdim=True)
        
        if self.return_map:
            return score_stack        
        return 1 - score_stack[:, 0].nanmean()