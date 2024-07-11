import tiktoken
import logging

class Calculator:
    """
    A class to estimate the cost of using different ChatGPT models based on the number of input and output tokens.

    Attributes:
        models (dict): A dictionary mapping model names to their respective input and output prices.
        tokenizers (dict): A cache for tokenizer instances for different models.
    """
    def __init__(self, max_cached_tokenizers=2):
        """
        Initializes the Calculator with supported models and their respective pricing.
        """
        self.models = {
            "gpt-4o": {"input_price": 5, "output_price": 15},
            "gpt-3.5-turbo-0125": {"input_price": 0.5, "output_price": 1.5},
            "gpt-3.5-turbo-instruct": {"input_price": 1.5, "output_price": 2}
        }
        self.tokenizers = {}
        self.max_cached_tokenizers = max_cached_tokenizers
        logging.basicConfig(level=logging.INFO)

    def get_tokenizer(self, model: str):
        """
        Retrieves the tokenizer using tiktoken library for a given model, caching it if not already present.

        Args:
            model (str): The model name for which to get the tokenizer.

        Returns:
            The tokenizer instance for the specified model.

        Raises:
            ValueError: If the model is not supported.
        """

        if model not in self.tokenizers:
            try:
                if model not in self.models:
                    raise ValueError("Unsupported model.")
                self.tokenizers[model] = tiktoken.encoding_for_model(model)
                if len(self.tokenizers) > self.max_cached_tokenizers:
                    self.tokenizers.pop(next(iter(self.tokenizers)))
                logging.info(f"Tokenizer for {model} loaded.")
            except Exception as e:
                logging.error(f"Error loading tokenizer for {model}: {e}")
                raise
        return self.tokenizers[model]

    def cost_estimate(self, model: str, input_text: str, output_text: str = "", info_text = False) -> str:
        """
        Estimates the cost for a given input and output text using a specified GPT model.

        Args:
            model (str): The GPT model to use for estimation.
            input_text (str): The input text.
            output_text (str): The output text (optional).
            info_text (bool): Choose to print or not a str report (optional)

        Returns:
            A dict detailing the estimated costs.

        Raises:
            ValueError: If the model is not supported.
        """
        if model not in self.models:
            raise ValueError("Unsupported model.")
        
        output = {}
        tokenizer = self.get_tokenizer(model)
        output["count_token_input"] = len(tokenizer.encode(input_text))
        output["count_token_output"] = len(tokenizer.encode(output_text))

        output["cost_token_input"] = output["count_token_input"] / 1000000 * self.models[model]["input_price"]
        output["cost_token_output"] = output["count_token_output"] / 1000000 * self.models[model]["output_price"]
        output["total_cost"] = output["cost_token_input"] + output["cost_token_output"]

        if info_text:
            rapport = (f"Input cost: {output['cost_token_input']:.3f}$ (rounded) ({output['count_token_input']} tokens). "
                       f"Output cost: {output['cost_token_output']:.3f}$ (rounded) ({output['count_token_output']} tokens). "
                       f"Total cost: {output['total_cost']:.3f}$ (rounded)."
                       "Please note that these costs are estimates and may vary depending on the actual response from OpenAi API.")
    
            if not output_text:
                rapport += (" Warning: No output example provided. "
                            "The actual cost could be higher due to the output tokens not included in this estimate.\n")
            print(rapport)
        return output
