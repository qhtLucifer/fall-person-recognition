from models.SGN.backbone import SGN
import torch
import os

class ActionRecognition():

    def __init__(self,args) -> None:

        self.time_range = args.seg
        self.num_joint = args.num_joint
        checkpoint_file = args.classifier_weight_path
        self.channels  = args.channels
        checkpoint = torch.load(checkpoint_file,map_location=args.device)
        self.model = SGN(args, False)
        
        self.model.load_state_dict(checkpoint)
        self.model.eval()
        labels_path = args.labels_path 
        with open(labels_path, 'r') as f:

            self.labels = f.readlines()

    def infer(self, frames)->str:

        assert len(frames) == self.time_range, "The length of frames should as same as " + str(self.time_range)
        
        frames_preprocessed = self.preprocess(frames = frames)
        results = torch.nn.functional.softmax(self.model(frames_preprocessed),dim = 1)[0]
        idx = torch.argmax(results)
        prob = torch.max(results)
        if idx == 42:
            print('FALL!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
        return self.labels[idx.item()][:-1], round(prob.item(),2)

    def preprocess(self,frames:torch.Tensor):

        # shape: [time range, num joint, channels] -> [1 ,time range, num joint * channels]

        frames = frames.view((1, self.time_range, self.num_joint * self.channels)) 

        return frames


        