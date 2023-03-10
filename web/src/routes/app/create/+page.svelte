<script>

    import { pb, currentUser } from '../../../lib/pocketbase'


    let loading = false;

    
    let name = ""
    let os = ""


    const createMachine = async () => {

        loading = true

        // console.log(os)
        // console.log(name)

        await fetch("http://localhost:5000/createvm", {
            method: "POST", // or 'PUT'
            headers: {
                "Content-Type": "application/json",
                "Authorization": "Bearer" + pb.authStore.token
            },
            body: JSON.stringify({
                "name": name,
                "os": os
            }),
        })
        .then((response) => {
            return response.json()
            
        })
        .then((data) => {
            console.log("Success:", data);
            createMachinePB(data.id, data.ip, name, os)
        })
        .catch((error) => {
            console.error("Error:", error);
        });

        // console.log()

        loading = false

    }

    const createMachinePB = async (id, ip, name, os) => {

        // example create data
        const data = {
            "machineID": id,
            "name": name,
            "user": pb.authStore.model.id,
            "os": os,
            "ip": ip
        };

        const record = await pb.collection('machines').create(data);

    }

</script>

<h1 class="text-3xl font-bold text-center p-5 pb-10">Create New Machine</h1>

{#if loading}

    <div class="grid justify-center">
        <h1 class="text-center pb-5 text-green-500">Provisioning...</h1>
        <progress class="progress w-56"></progress>
    </div>

{:else}
    <div class="grid justify-center gap-5">
        <!-- <div class="grid grid-cols-2 w-96 gap-5"> -->
            <div class="form-control w-full max-w-xs">
                <!-- svelte-ignore a11y-label-has-associated-control -->
                <label class="label">
                <span class="label-text">Machine Name</span>
                </label>
                <input bind:value={name} type="text" placeholder="Type here" class="input input-bordered w-full max-w-xs" />
            </div>

            <!-- <div class="form-control w-full max-w-xs">
                <label class="label">
                <span class="label-text">Root Password</span>
                </label>
                <input type="text" placeholder="Type here" class="input input-bordered w-full max-w-xs" />
            </div> -->

            
        <!-- </div> -->

        <div class="flex justify-center">
            <div class="form-control w-full max-w-xs">
                <!-- svelte-ignore a11y-label-has-associated-control -->
                <label class="label">
                <span class="label-text">Choose OS</span>
                </label>
                <select bind:value={os} class="select select-bordered w-full max-w-xs">
                    <option disabled selected>Choose OS</option>
                    <option>LinuxLite</option>
                    <option>Kali</option>
                </select>
        
            </div>
        </div>
        <div class="flex justify-center p-10">
            <button on:click={createMachine} class="btn btn-outline btn-success">Submit</button>
        </div>
    </div>
{/if}