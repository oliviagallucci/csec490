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
        goto(`/app/admin/${$page.params.org}/class/${c.slug}`);
    }
</script>
<SearchBox bind:value={search} />
<br>

{#each classes as c}
    {#if c.name.includes(search) || (c.slug ?? '').includes(search)}
    <ClassCard c={c}>
        <div slot="actions">
            <Button style="primary" callback={()=>{goToClass(c);}}>Edit</Button>
        </div>
    </ClassCard>
    {/if}
{/each}
