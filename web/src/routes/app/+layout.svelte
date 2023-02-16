<script>
    import { goto } from "$app/navigation";
    import { pb } from "$lib/pocketbase.js"

    const logout = () => {
        pb.authStore.clear()

        goto('/login')
    }

</script>


<div class="navbar bg-base-100">
    <div class="flex-1">
        <a class="btn btn-ghost normal-case text-xl" href="/app">Whale Cloud</a>
    </div>
    <div class="flex-none">
        <ul class="menu menu-horizontal px-1">
            <li><a href="/app/machines">Machines</a></li>
            <li><a href="/app/create">Create</a></li>
            <button on:click={logout} class="btn btn-outline">Logout</button>
        </ul>
    </div>
</div>

<slot/>