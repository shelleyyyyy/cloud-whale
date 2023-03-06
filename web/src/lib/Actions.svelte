<script>
    import { onMount } from 'svelte'
    import { pb } from './pocketbase'
    export let id;

    let state = ""

    onMount(async () => {
		const res = await fetch(`http://localhost:5000/info`, {
            method: "POST", // or 'PUT'
            headers: {
                "Content-Type": "application/json",
                "Authorization": "Bearer" + pb.authStore.token
            },
            body: JSON.stringify({
                "id": id
            }),
        });
		state = await res.json();
        console.log(state)

        console.log(pb.authStore.token)
	});

    const startMachine = async (id) => {
        fetch("http://localhost:5000/startvm", {
            method: "POST", // or 'PUT'
            headers: {
                "Content-Type": "application/json",
                "Authorization": "Bearer" + pb.authStore.token
            },
            body: JSON.stringify({
                "id": id
            }),
        })
        .then((data) => {
            console.log("Success:", data);
            state = "on"
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
                "Authorization": "Bearer" + pb.authStore.token
            },
            body: JSON.stringify({
                "id": id
            }),
        })
        .then((data) => {
            console.log("Success:", data);
            state = "off"
        })
        .catch((error) => {
            console.error("Error:", error);
        });

    }

    const removeMachine = async (name) => {
        fetch("http://localhost:5000/deletevm", {
            method: "POST", // or 'PUT'
            headers: {
                "Content-Type": "application/json",
                "Authorization": "Bearer" + pb.authStore.token
            },
            body: JSON.stringify({
                "name": name
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


<th>
    {#if state == "on"}
        <button on:click={stopMachine(id)} class="btn btn-outline btn-warning btn-xs">stop</button>
    {:else}
        <button on:click={startMachine(id)} class="btn btn-outline btn-success btn-xs">start</button>
    {/if}
    
    <button class="mx-5 btn btn-outline btn-error btn-xs">remove</button>
</th>