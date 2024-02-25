<script>
    import CardTemplate from "./CardTemplate.svelte";
    /**
     * @property mode {('view'|'edit')}
     */
    export var mode = "view";
    export var config = {
        "content":""
    }
</script>

<CardTemplate>
    {#if mode == "edit"}
        <textarea class="font-code w-full" rows="5" bind:value={config["content"]}/>
    {:else}
        <div class="prose">{@html config["content"]}</div>
    {/if}
</CardTemplate>
