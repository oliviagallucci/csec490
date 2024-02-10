<script>
    import CardTemplate from "./CardTemplate.svelte";


    
    let content = `<h1>Header</h1><p>Paragraph</p>`;
</script>

<CardTemplate><div class="prose">{@html content}</div></CardTemplate>