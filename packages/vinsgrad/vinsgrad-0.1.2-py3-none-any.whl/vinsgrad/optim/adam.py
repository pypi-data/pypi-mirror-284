from typing import List, Dict, Any
from vinsgrad.core import Tensor
from vinsgrad.optim._optimizer import Optimizer
import numpy as np

class Adam(Optimizer):
    """
    Adam optimizer implementation.
    """

    def __init__(self, parameters: List[Tensor], lr: float = 0.001, betas: tuple = (0.9, 0.999), eps: float = 1e-8, weight_decay: float = 0) -> None:
        """
        Initializes the Adam optimizer.

        Args:
            parameters (List[Tensor]): The list of parameters to optimize.
            lr (float): The learning rate (default: 0.001).
            betas (tuple): Coefficients used for computing running averages of gradient and its square (default: (0.9, 0.999)).
            eps (float): Term added to the denominator to improve numerical stability (default: 1e-8).
            weight_decay (float): Weight decay (L2 penalty) (default: 0).
        """
        super().__init__(parameters, lr)
        if not 0.0 <= lr:
            raise ValueError(f"Invalid learning rate: {lr}")
        if not 0.0 <= eps:
            raise ValueError(f"Invalid epsilon value: {eps}")
        if not 0.0 <= betas[0] < 1.0:
            raise ValueError(f"Invalid beta parameter at index 0: {betas[0]}")
        if not 0.0 <= betas[1] < 1.0:
            raise ValueError(f"Invalid beta parameter at index 1: {betas[1]}")
        if not 0.0 <= weight_decay:
            raise ValueError(f"Invalid weight_decay value: {weight_decay}")
        
        self.betas = betas
        self.eps = eps
        self.weight_decay = weight_decay
        self.state = {}
        self.t = 0

    def state_dict(self) -> Dict[str, Any]:
        """
        Returns the state of the optimizer as a dictionary.

        Returns:
            Dict[str, Any]: The state of the optimizer.
        """
        return {
            'lr': self.lr,
            'betas': self.betas,
            'eps': self.eps,
            'weight_decay': self.weight_decay,
            'state': self.state,
            't': self.t
        }

    def load_state_dict(self, state_dict: Dict[str, Any]) -> None:
        """
        Loads the optimizer state.

        Args:
            state_dict (Dict[str, Any]): The state of the optimizer.
        """
        self.lr = state_dict['lr']
        self.betas = state_dict['betas']
        self.eps = state_dict['eps']
        self.weight_decay = state_dict['weight_decay']
        self.state = state_dict['state']
        self.t = state_dict['t']

    def step(self) -> None:
        """
        Performs a single optimization step.
        """
        self.t += 1
        for p in self.parameters:
            if p.grad is None:
                continue
            grad = p.grad.astype(np.float32)
            
            if p not in self.state:
                self.state[p] = {
                    'step': 0,
                    'exp_avg': np.zeros_like(p.data, dtype=np.float32),
                    'exp_avg_sq': np.zeros_like(p.data, dtype=np.float32)
                }
            
            state = self.state[p]
            state['step'] += 1
            
            if self.weight_decay != 0:
                grad = grad + self.weight_decay * p.data
            
            exp_avg, exp_avg_sq = state['exp_avg'], state['exp_avg_sq']
            beta1, beta2 = self.betas
            
            exp_avg = beta1 * exp_avg + (1 - beta1) * grad
            exp_avg_sq = beta2 * exp_avg_sq + (1 - beta2) * np.square(grad)
            
            bias_correction1 = 1 - beta1 ** state['step']
            bias_correction2 = 1 - beta2 ** state['step']
            
            step_size = self.lr * np.sqrt(bias_correction2) / bias_correction1
            
            p.data -= step_size * exp_avg / (np.sqrt(exp_avg_sq) + self.eps)
            
            state['exp_avg'] = exp_avg
            state['exp_avg_sq'] = exp_avg_sq