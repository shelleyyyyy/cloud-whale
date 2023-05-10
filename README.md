# Instructions to use:

This project requires that you export the VMs you want to use on Cloud Whale into the "VMs" directory. There are none by default so it will not function. 

1. In Virtual Box right click on the VMs you want to use and click "Export to OCI". Change the output directory to the "VMs" directory in this repository.

2. Update the config


# flask boot

flask --app serve run --host=0.0.0.0

# web boot

npm run dev -- --host

# pb boot

./pocketbase serve --http=0.0.0.0:8090