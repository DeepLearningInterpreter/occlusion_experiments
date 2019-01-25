# occlusion_experiments
This repository contains supplementary material to a paper that is currently under review for ICML 2019. Among other content, the code and data, which are needed to reproduce the results, are included.

This repository allows for fast reproduction of the occlusion experiments. No downloads and installations are required because the code can be ran in the cloud for free, using Google Colaboratory. 

The only thing you have to do to get started is:
1. Navigate to the "colab_notebooks" folder.
2. Open one of the notebooks by clicking on it.
3. Click the blue "Open in Colab" button at the beginning of the notebook.
4. Follow the instructions in the notebook (or just run all cells of the notebook by pressing ctrl+F9).
5. Recommended: play around with the parameters as explained in the notebooks. 
	
Additionally, notebooks are provided that can be used to reproduce the model training and tuning processes. These notebooks are also helpful for training and evaluating models with new, improved, and/or different configurations. These configurations have to be specified in a ".config" file.

In the "main_content/assortment of heatmaps" folder, a number of heatmaps can be found, many of which are not included in the paper.

This repository will not be changed anymore until the reviewing period for ICML 2019 is over. This period ends around the 24th of April.

The work here relies for a great deal on the TensorFlow object detection API (https://github.com/tensorflow/models/tree/master/research/object_detection). So, thanks a lot to the developers and maintainers of that repository.
