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
   * @type {any[]}
   */
  var cards: any[] = [
  ];



  onMount(()=>{
  loadLesson();


});

</script>

<PageTitle>
  <span slot="title">{lesson?.name}</span>
  <span slot="subtitle">0% Complete</span>
  <span slot="actions">
      
  </span>
</PageTitle>
{#each cards as c, index (index)}

  

  {#if c["type"] == "ctf"}
      <CtfCard mode="view" bind:config={cards[index]["config"]} classId={$page.params["classid"]} lessonId={$page.params["lessonid"]}/>
  {:else if c["type"] == "text"}
      <TextCard mode="view" bind:config={cards[index]["config"]} />
  {:else if c["type"] == "vm"}

      <ProvisionCard mode="view" bind:config={cards[index]["config"]} />
  {/if}
  <br>
  
{/each}


