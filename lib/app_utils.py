import torch
from lib.utils import cells_to_bboxes, non_max_suppression
def get_eval_boxes(x, model, anchors, iou_threshold, threshold, device="cuda"):
    model.eval()
    x = x.to(device)
    tmp = torch.reshape(x, (1, x.size()[0], x.size()[1], x.size()[2]))
    all_pred_boxes = []
    train_idx = 0
    with torch.no_grad():
        preditcions = model(tmp)
    batch_size = tmp.shape[0]
    bboxes = bboxes = [[] for _ in range(batch_size)]
    for i in range(3):
        S = preditcions[i].shape[2]
        anchor = torch.tensor([*anchors[i]]).to(device) * S
        boxes_scale_i = cells_to_bboxes(
            preditcions[i], anchor, S=S, is_preds=True

        )
        for idx, (box) in enumerate(boxes_scale_i):
            bboxes[idx] += box

    for idx in range(batch_size):
        nms_boxes = non_max_suppression(
            bboxes[idx],
            iou_threshold=iou_threshold,
            threshold=threshold,
            box_format="midpoint"
        )

        for nms_box in nms_boxes:
            all_pred_boxes.append([train_idx] + nms_box)
            train_idx += 1
    model.train()
    return all_pred_boxes