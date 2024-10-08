_base_ = [
    '../_base_/models/retinanet_r50_fpn.py',
    '../_base_/datasets/ShipRSImageNet_Augmented_MatchedRes_Level3_combined_categories_detection.py',
    '../_base_/schedules/schedule_100e.py', '../_base_/default_runtime.py'
]

model = dict(
    pretrained='torchvision://resnet101',
    backbone=dict(depth=101),
    bbox_head=dict(num_classes=10))


# optimizer
optimizer = dict(type='SGD', lr=0.02/4, momentum=0.9, weight_decay=0.0001)

checkpoint_config = dict(interval=20)
evaluation = dict(interval=50, metric='bbox')	# 评价指标
lr_config = dict(
    policy='step',
    warmup='linear',
    warmup_iters=500,
    warmup_ratio=0.001,
    step=[80, 90])
dist_params = dict(backend='nccl')
total_epochs = 100
