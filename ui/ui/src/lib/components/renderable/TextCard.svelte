<script>
    import CardTemplate from "./CardTemplate.svelte";


    
    let content = `<h1>Header</h1><p>Paragraph</p>`;
</script>

<CardTemplate>{@html content}</CardTemplate>