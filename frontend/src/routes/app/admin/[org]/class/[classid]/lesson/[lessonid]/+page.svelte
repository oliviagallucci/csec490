<script>
    import AddDivider from "$lib/components/generic/AddDivider.svelte";
    import Button from "$lib/components/generic/Button.svelte";
    import PageTitle from "$lib/components/generic/PageTitle.svelte";
    import CtfCard from "$lib/components/renderable/CTFCard.svelte";
    import ProvisionCard from "$lib/components/renderable/ProvisionCard.svelte";
    import TextCard from "$lib/components/renderable/TextCard.svelte";
    import { json } from "@sveltejs/kit";

    

    /**
     * @property mode {('view'|'edit')}
     */
    var mode = "edit";
    /**
     * @type {any[]}
     */
    var cards = [
        {
            type: "ctf",
            config: {
                title: "Test",
                description: "Config",
                flag: "RS{CONFIG}",
            },
        },
        {
            type: "text",
            config: {
                value: "",
            },
        },
        {
            type: "vm",
            config:{
                image:""
            }
        }
    ];

    function toggleView() {
        if (mode == "view") {
            mode = "edit";
        } else {
            mode = "view";
        }
    }
    function addElement(index, type){
        if (type == "ctf"){
            cards.splice(index, 0,{
                type:"ctf",
                config: {
                title: "Test",
                description: "Config",
                flag: "RS{CONFIG}",
            },
            })

        }else if(type == "text"){
            cards.splice(index, 0,{
                type:"text",
                config: {
                value: "",
            },})
        }else if(type == "vm"){
            cards.splice(index, 0,{
                type:"vm",
                config: {
                image: "",
            },})
        }
       cards = cards;
    }
</script>

<PageTitle>
    <span slot="title">Intro to Linux</span>
    <span slot="actions">
        <Button>Save</Button>&nbsp;
        <Button style="secondary">Publish</Button>&nbsp;
        <Button
            style="secondary"
            callback={() => {
                toggleView();
            }}>{mode == "view" ? "Edit":"Preview"}</Button
        >
    </span>
</PageTitle>
{#each cards as c, index (index)}
    <AddDivider onAdd={(type)=>{
        addElement(index, type);
    }}/>

    {#if c["type"] == "ctf"}
        <CtfCard {mode} bind:config={cards[index]["config"]} />
    {:else if c["type"] == "text"}
        <TextCard {mode} bind:config={cards[index]["config"]} />
    {:else if c["type"] == "vm"}

        <ProvisionCard {mode} bind:config={cards[index]["config"]} />
    {/if}
    
{/each}
<AddDivider onAdd={(type)=>{
    addElement(cards.length+1, type);
}}/>
