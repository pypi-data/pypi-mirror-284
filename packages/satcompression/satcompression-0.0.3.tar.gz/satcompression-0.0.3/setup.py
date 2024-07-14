# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['satcompression']

package_data = \
{'': ['*']}

install_requires = \
['numpy>=1.25.2', 'sortedcontainers>=2.4.0', 'tqdm>=4.66.4']

setup_kwargs = {
    'name': 'satcompression',
    'version': '0.0.3',
    'description': 'A python package to compress sat data',
    'long_description': '# satcompression\nEfficient decomposition of satellite images in a Quad-Tree structure\n\n\n## Installation\n\n```bash\npip install satcompression\n```\n\n## Usage\n\nCompression and decompression of satellite images using the Quad-Tree structure.\n\n```python\nimport satcompression\nimport rasterio as rio\n\n# Load an image\nwith rio.open(\'path/to/image.tif\') as src:\n    image_meta = src.meta\n    image_data = src.read()\n\n# Compress the image\nimage_data_compress = satcompression.compress_and_encode_image_data(\n    image_data=image_data, detail_error_threshold=20\n)\n\n# Decompress the image\nimage_data_decompress = satcompression.reconstruct_image_data(\n    data=image_data_compress, dtype=image_data.dtype, nchannels = image_data.shape[0]\n)\n```\n\n![image](docs/images/visual_comparison.png)\n\nObtain the pseudo-mtf from the quadtree structure.\n\n```python\nimport satcompression\nimport matplotlib.pyplot as plt\n\nwith rio.open(\'path/to/image.tif\') as src:    \n    image_data = src.read()\n\nmtf_values1, x_axis1 = satcompression.quadtree_mtf(image_data, 10, detail_error_threshold=20)\nmtf_values2, x_axis2 = satcompression.quadtree_mtf(image_data, 10, detail_error_threshold=10)\nmtf_values3, x_axis3 = satcompression.quadtree_mtf(image_data, 10, detail_error_threshold=5)\n\nplt.plot(x_axis1, mtf_values1, label="Detail Error Threshold: 0.002")\nplt.plot(x_axis2, mtf_values2, label="Detail Error Threshold: 0.001")\nplt.plot(x_axis3, mtf_values3, label="Detail Error Threshold: 0.0005")\nplt.legend()\nplt.ylim(0, 1.2)\nplt.title("Pseudo-MTF obtained from the quadtree decomposition")\nplt.show()\n```\n\n![image](docs/images/mtf_comparison.png)\n\nObtain the classification of the quadtree nodes.\n\n```python\nimport satcompression\n\nwith rio.open(\'path/to/image.tif\') as src:    \n    image_data = src.read()\n\nsatcompression.create_classification_map(image_data, detail_error_threshold=20)\n```\n\n![image](docs/images/classification_map.png)\n',
    'author': 'Cesar Aybar',
    'author_email': 'fcesar.aybar@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/csaybar/satcompression',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
