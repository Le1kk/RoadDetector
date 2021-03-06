import argparse

parser = argparse.ArgumentParser()
arg = parser.add_argument
arg('--gpu', default="0")
arg('--epochs', type=int, default=100)
arg('--fold', default='0')
arg('--n_folds', type=int, default=4)
arg('--freeze_till_layer', default='input_1')
arg('--preprocessing_function', default='tf')
arg('--weights')
arg('--city')
arg('--input_size', type=int, default=1300)
arg('--padded_size', type=int, default=1312)
arg('--save_epochs')
arg('--learning_rate', type=float, default=0.0003)
arg('--crop_size', type=int, default=256)
arg('--crops_per_image', type=int, default=1)
arg('--batch_size', type=int, default=1)
arg('--loss_function', default='bce_dice')
arg('--clr')
arg('--schedule')
arg('--optimizer')
arg('--num_workers', type=int, default=8)
arg('--clahe', action='store_true')
arg('--ohe_city',  action='store_true')
arg('--stretch_and_mean', action='store_true')
arg('--network', default='inception_linknet')
arg('--alias', default='full')
arg('--steps_per_epoch', type=int, default=1000)
arg('--seed', type=int, default=777)
arg('--models_dir', default='trained_models')
arg('--data_dirs', nargs='+')

#prediction
arg('--out_dir_name')
arg('--city_id')
arg('--ensembling_dirs')
arg('--dirs_to_process', nargs='+')
arg('--output_file')
arg('--wdata_dir')


args = parser.parse_args()
