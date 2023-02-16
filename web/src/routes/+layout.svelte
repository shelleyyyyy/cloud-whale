<script>
    import "../app.css";
    import { onMount } from "svelte";
    import { goto } from '$app/navigation';
    import { pb } from '$lib/pocketbase.js'
    
    onMount(() => {
      if(pb.authStore.isValid){
        goto('/app')
      } else {
        goto('/login')
      }
    })
</script>

<slot/>