<script>
    import CardTemplate from "./CardTemplate.svelte";
    import Editor from "@tinymce/tinymce-svelte";
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
    <Editor
    channel="6"
    id="uuid"
   
    scriptSrc="https://cdnjs.cloudflare.com/ajax/libs/tinymce/6.8.3/tinymce.min.js"
    modelEvents="input change undo redo"
    bind:value={config["content"]}
  />
    {:else}
        <div class="prose min w-full max-w-full">{@html config["content"]}</div>
    {/if}
</CardTemplate>
