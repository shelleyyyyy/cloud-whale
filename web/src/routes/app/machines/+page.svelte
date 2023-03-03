
<script>

    import { onMount } from 'svelte'

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
		const res = await fetch(`http://localhost:5000/list`);
		machines = await res.json();
        console.log(machines)
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
            console.log("Success:", data);
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
            <th>ID</th>
            <!-- <th>IP</th> -->
            <th>State</th>
            <th>Actions</th>
            </tr>
        </thead>
        <tbody>
            <!-- row 1 -->
            {#each machines as m}
                <tr>
                    <td>
                        {m.title}
                    </td>
                    <td>
                        {m.id}
                    </td>
                    <!-- <td>
                        {m.ip}
                    </td> -->
                    <td>
                        {m.state}
                    </td> 
                    <th>
                        <!-- {#if m.state == "on"} -->
                            <button on:click={stopMachine(m.id)} class="btn btn-outline btn-warning btn-xs">stop</button>
                        <!-- {:else} -->
                            <button on:click={startMachine(m.id)} class="btn btn-outline btn-success btn-xs">start</button>
                        <!-- {/if} -->
                        <!-- <button class="mx-5 btn btn-outline btn-error btn-xs">remove</button> -->
                    </th>
                </tr>
            {/each}
            
        </tbody>
    </table>
  </div>