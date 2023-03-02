
<script>

    const machines = [
        {
            "name": "Kali Test",
            "image": "Kali Linux",
            "ip": "192.168.0.1",
            "state": "off"
        },
        {
            "name": "Ubuntu Test",
            "image": "Ubuntu 22.04",
            "ip": "192.168.0.2",
            "state": "on"
        },
        {
            "name": "Cent Test",
            "image": "Cent OS",
            "ip": "192.168.0.3",
            "state": "off"
        }
    ]

</script>


<h1 class="text-3xl font-bold text-center p-5">Machines</h1>

<div class="overflow-x-auto w-full p-10">
    <table class="table w-full">
      <!-- head -->
        <thead>
            <tr>
            <th>Name</th>
            <th>Image</th>
            <th>IP</th>
            <th>State</th>
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
                        {m.image}
                    </td>
                    <td>
                        {m.ip}
                    </td>
                    <td>
                        {m.state}
                    </td>
                    <th>
                        {#if m.state == "on"}
                            <button class="btn btn-outline btn-warning btn-xs">stop</button>
                        {:else}
                            <button class="btn btn-outline btn-success btn-xs">start</button>
                        {/if}
                        <button class="mx-5 btn btn-outline btn-error btn-xs">remove</button>
                    </th>
                </tr>
            {/each}
            
        </tbody>
    </table>
  </div>