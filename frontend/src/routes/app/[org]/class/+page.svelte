<script lang="ts">
   

/** @type {import('./$types').PageData} */
    export let data: PageData;
</script>

{#each data.class as c}
    <h1>{c.name}</h1>
    <p>{c.description}</p>
{/each}

