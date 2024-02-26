from poseidon.generation.instance_generator import InstanceGenerator
from poseidon.extraction.instance_extractor import InstanceExtractor
from poseidon.utils.normalization import normalize
from shiprsimagenet import ShipRSImageNet


CLASS_TO_AUGMENT = 'Fishing Vessel'

SEED = 3030292994


if __name__ == '__main__':
    original_dataset = ShipRSImageNet('ShipRSImageNet_V1')

    with open('selected_for_augmentation.txt', 'r') as f:
        images_to_process = f.read().splitlines()
    
    with open('selected_for_augmentation_matched_resolution.txt', 'r') as f:
        matched_resolution_images_to_process = f.read().splitlines()

    # The original normalization method described by POSEIDON is not a good fit for the ShipRSImageNet dataset
    # We'll instead normalize images based on the source and destination spatial resolutions
    #print('Normalizing images...')
    #normalize(original_dataset.root_path, "ShipRSImageNet_V1_Normalized", images_to_process, 'train_level_2')
    #print()

    print('Compiling source instances for generator...')
    extractor = InstanceExtractor(original_dataset)
    extractor.extract_instances(CLASS_TO_AUGMENT, 'fishing_vessel_instances')
    print()

    # See notebook for selection of these args
    target_avg_of_instances_per_image = 3
    total_instances_to_add = len(images_to_process) * target_avg_of_instances_per_image
    min_instances_per_image = 1
    max_instances_per_image = 5

    print('Augmenting images...')
    generator = InstanceGenerator('Fishing Vessel', 'fishing_vessel_instances', seed=SEED)
    generator.augment(original_dataset, "ShipRSImageNet_V1_Augmented", images_to_process,
                      total_instances_to_add,
                      min_instances_per_image,
                      max_instances_per_image,
                     ) 
    
    total_instances_to_add = len(matched_resolution_images_to_process) * target_avg_of_instances_per_image
    print('Augmenting images with matched resolution to extracted instances...')
    generator.augment(original_dataset, "ShipRSImageNet_V1_Augmented_MatchedRes", matched_resolution_images_to_process,
                      total_instances_to_add,
                      min_instances_per_image,
                      max_instances_per_image,
                     )
    print()
