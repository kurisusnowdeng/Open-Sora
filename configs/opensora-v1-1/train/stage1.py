# Define dataset
dataset = dict(
    # type="VariableVideoTextDataset",
    type="VideoTextDataset",
    data_path=None,
    # num_frames=None,
    num_frames=16,
    frame_interval=3,
    # image_size=(None, None),
    image_size=(512, 512),
    transform_name="resize_crop",
)
# IMG: 1024 (20%) 512 (30%) 256 (50%) drop (50%)
# bucket_config = {  # 1s/it
#     "144p": {1: (0.5, 48), 16: (1.0, 6), 32: (1.0, 3), 96: (1.0, 1)},
#     "256": {1: (0.5, 24), 16: (0.5, 3), 48: (0.5, 1), 64: (0.0, None)},
#     "240p": {16: (0.3, 2), 32: (0.3, 1), 64: (0.0, None)},
#     "512": {1: (0.4, 12)},
#     "1024": {1: (0.3, 3)},
# }
mask_ratios = {
    "mask_no": 0.75,
    "mask_quarter_random": 0.025,
    "mask_quarter_head": 0.025,
    "mask_quarter_tail": 0.025,
    "mask_quarter_head_tail": 0.05,
    "mask_image_random": 0.025,
    "mask_image_head": 0.025,
    "mask_image_tail": 0.025,
    "mask_image_head_tail": 0.05,
}

# Define acceleration
num_workers = 4
# num_workers = 8
# num_bucket_build_workers = 16
# dtype = "bf16"
dtype = "fp16"
grad_checkpoint = False
plugin = "zero2"
sp_size = 1

# Define model
model = dict(
    type="STDiT2-XL/2",
    from_pretrained="./pretrained_models/stdit/OpenSora/OpenSora-v1-HQ-16x512x512.pth",
    input_sq_size=512,  # pretrained model is trained on 512x512
    qk_norm=True,
    enable_flashattn=True,
    enable_layernorm_kernel=True,
)
vae = dict(
    type="VideoAutoencoderKL",
    # from_pretrained="stabilityai/sd-vae-ft-ema",
    from_pretrained="./pretrained_models/stabilityai/sd-vae-ft-ema",
    micro_batch_size=4,
    local_files_only=True,
)
text_encoder = dict(
    type="t5",
    # from_pretrained="DeepFloyd/t5-v1_1-xxl",
    from_pretrained="./pretrained_models/t5_ckpts/t5-v1_1-xxl",
    model_max_length=200,
    shardformer=True,
    local_files_only=True,
)
scheduler = dict(
    type="iddpm",
    timestep_respacing="",
)

# Others
seed = 42
outputs = "outputs"
wandb = False

# epochs = 1000
# log_every = 10
# ckpt_every = 500
# load = None

epochs = 10
log_every = 10
ckpt_every = 100
load = None

batch_size = 1
lr = 2e-5
grad_clip = 1.0
