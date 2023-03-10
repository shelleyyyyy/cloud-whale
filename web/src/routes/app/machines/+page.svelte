
<script>
    import { pb } from '../../../lib/pocketbase'
    import { onMount } from 'svelte'
    import Actions from '../../../lib/Actions.svelte';

    let machines = [];
    // const machines = [
    //     {
    //         "name": "Kali Test",
    //         "image": "Kali Linux",
    //         "ip": "192.168.0.1",
    //         "state": "off"
    //     },
    //     {
    //         "name": "Ubuntu Test",
    //         "image": "Ubuntu 22.04",
    //         "ip": "192.168.0.2",
    //         "state": "on"
    //     },
    //     {
    //         "name": "Cent Test",
    //         "image": "Cent OS",
    //         "ip": "192.168.0.3",
    //         "state": "off"
    //     }
    // ]

	onMount(async () => {
		// const res = await fetch(`http://localhost:5000/list`);
		// machines = await res.json();
        // console.log(machines)

        const records = await pb.collection('machines').getFullList(200 /* batch size */, {
            sort: '-created',
        });

        machines = records

        pb.collection('machines').subscribe('*', function (e) {
            machines = machines.filter((m) => m.id !== e.record.id);
        });
	});

    

    const startMachine = async (id) => {
        fetch("http://localhost:5000/startvm", {
            method: "POST", // or 'PUT'
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                "id": id
            }),
        })
        .then((data) => {
            // console.log("Success:", data);
        })
        .catch((error) => {
            console.error("Error:", error);
        });

    }

    const stopMachine = async (id) => {
        fetch("http://localhost:5000/stopvm", {
            method: "POST", // or 'PUT'
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                "id": id
            }),
        })
        .then((data) => {
            console.log("Success:", data);
        })
        .catch((error) => {
            console.error("Error:", error);
        });

    }
    



</script>


<h1 class="text-3xl font-bold text-center p-5">Machines</h1>

<div class="overflow-x-auto w-full p-10">
    <table class="table w-full">
      <!-- head -->
        <thead>
            <tr>
            <th>Name</th>
            <th>OS</th>
            <th>ID</th>
            <th>IP</th>
            <th>Actions</th>
            </tr>
        </thead>
        <tbody>
            <!-- row 1 -->
            {#each machines as m}
                <tr>
                    <td>
                        {m.name}
                    </td>
                    <td>
                        {m.os}
                    </td>
                    <td>
                        {m.machineID}
                    </td>
                    <td>
                        {m.ip}
                    </td>

                    <Actions recordID={m.id} id={m.machineID} name={m.name}/>
                    
                </tr>
            {/each}
            
        </tbody>
    </table>
  </div>