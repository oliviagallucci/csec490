<script lang="ts">
    import { goto } from '$app/navigation';
    import { page } from '$app/stores';
    import * as api from '$lib/api';
    import ClassCard from '$lib/components/contentTypeCards/ClassCard.svelte';
    import Button from '$lib/components/generic/Button.svelte';
    import SearchBox from "$lib/components/generic/SearchBox.svelte";
    var search = "";

    var classes: api.Class[] = [];

    api.getClasses().then((res)=>{
        classes=res;
    });

    function goToClass(c: api.Class){
        goto(`/app/${$page.params.org}/class/${c.id}`);
    }
</script>
<SearchBox bind:value={search} />
<br>
<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3  gap-4">


{#each classes as c}
    {#if c.name.includes(search) || (c.slug ?? '').includes(search)}
    <ClassCard c={c}>
        <div slot="actions">
            <Button style="primary" callback={()=>{goToClass(c);}}>Open</Button>
        </div>
    </ClassCard>
    {/if}
{/each}
</div>