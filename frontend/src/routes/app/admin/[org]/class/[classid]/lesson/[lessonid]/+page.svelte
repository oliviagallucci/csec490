<script lang="ts">
    import * as api from "$lib/api";
    import AddDivider from "$lib/components/generic/AddDivider.svelte";
    import Button from "$lib/components/generic/Button.svelte";
    import PageTitle from "$lib/components/generic/PageTitle.svelte";
    import CtfCard from "$lib/components/renderable/CTFCard.svelte";
    import ProvisionCard from "$lib/components/renderable/ProvisionCard.svelte";
    import TextCard from "$lib/components/renderable/TextCard.svelte";
    import { json } from "@sveltejs/kit";
    import { page } from "$app/stores";
    import { onMount } from "svelte";

    
    var lesson: api.Lesson | null = null;
    var lessonId = $page.params.lessonid;

   async function loadLesson() {
        api.getLessonById($page.params.classid, lessonId).then((res) => {
            lesson = res;
            if(res != null){
                var conf = res.config ? JSON.parse(res.config) : null;
                if (conf != null){
                    cards = conf["cards"];
                }
            }
            
        });
      
    }

    /**
     * @property mode {('view'|'edit')}
     */
    var mode = "edit";
    /**
     * @type {any[]}
     */
    var cards: any[] = [
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

    onMount(()=>{
    loadLesson();


});

async function saveLesson(){
    var conf = {
        cards: cards,
    }

    if (lesson != null) {
        lesson.config = JSON.stringify(conf);

        var res = await api.updateLesson($page.params.classid, lessonId, lesson);
        if (res != null){
        console.log("Saved");
    }
    }
    
}

async function publishLesson(){
    if(lesson != null){
        lesson.visible = !lesson.visible;
        await saveLesson();
    }
    
}

</script>

<PageTitle>
    <span slot="title">{lesson?.name}</span>
    <span slot="actions">
        <Button callback={()=>{saveLesson();}}>Save</Button>&nbsp;
        <Button style="secondary" callback={()=>{publishLesson();}}>{lesson?.visible ? "Unpublish":"Publish"}</Button>&nbsp;
        <Button
            style="secondary"
            callback={() => {
                toggleView();
            }}>{mode == "view" ? "Edit":"Preview"}</Button
        >
    </span>
</PageTitle>
{#each cards as c, index (index)}
{#if mode=="edit"}
<AddDivider onAdd={(type)=>{
    addElement(index, type);
}}/>
{:else}
<br />
{/if}
    

    {#if c["type"] == "ctf"}
        <CtfCard {mode} bind:config={cards[index]["config"]} />
    {:else if c["type"] == "text"}
        <TextCard {mode} bind:config={cards[index]["config"]} />
    {:else if c["type"] == "vm"}

        <ProvisionCard {mode} bind:config={cards[index]["config"]} />
    {/if}
    
{/each}
{#if mode=="edit"}
<AddDivider onAdd={(type)=>{
    addElement(cards.length+1, type);
}}/>
{/if}

