import torch
from mplug_owl.modeling_mplug_owl import MplugOwlForConditionalGeneration
from mplug_owl.tokenization_mplug_owl import MplugOwlTokenizer
from mplug_owl.processing_mplug_owl import MplugOwlImageProcessor, MplugOwlProcessor

pretrained_ckpt = 'MAGAer13/mplug-owl-llama-7b'
model = MplugOwlForConditionalGeneration.from_pretrained(
    pretrained_ckpt,
    torch_dtype=torch.bfloat16,
)
image_processor = MplugOwlImageProcessor.from_pretrained(pretrained_ckpt)
tokenizer = MplugOwlTokenizer.from_pretrained(pretrained_ckpt)
processor = MplugOwlProcessor(image_processor, tokenizer)