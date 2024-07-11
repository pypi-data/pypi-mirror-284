from setuptools import find_packages, setup

setup(
    name='netbox-multicast-stream-mapping',
    version='0.3',
    description='A Plugin to map multicast streams to netbox devices',
    install_requires=[],
    packages=find_packages(),
    include_package_data=True,
    package_data={
        'netbox_multicast_stream_mapping': ['templates/netbox_multicast_stream_mapping/*.html'],
    },
    zip_safe=False,
)

