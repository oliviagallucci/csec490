<script lang="ts">
    import Button from "$lib/components/generic/Button.svelte";
import PageTitle from "$lib/components/generic/PageTitle.svelte";
import * as api from '$lib/api';

import { page } from '$app/stores';
    import { onMount } from "svelte";

var c: api.Class | null = null;
var lessons: api.Lesson[] = [];

async function loadClass(){
    var temp = await api.getClassById($page.params.classid);
    
    c = temp;
}
async function loadLessons(){
    var temp = await api.getLessonsByClassId($page.params.classid);
    lessons = temp;
}

onMount(()=>{
    loadClass();
    loadLessons();
});

</script>
<PageTitle>
    <span slot="title">{c?.name}</span>

    <span slot="actions"><Button>New Lesson</Button></span>
</PageTitle>
<div class="flex flex-col md:flex-row">
    <!--
    <div class="flex-auto">
        <h3 class="text-2xl font-bold">Today</h3>
        <ul role="list" class="space-y-3">
            <li class="overflow-hidden rounded-md bg-white px-6 py-4 shadow">
              <p>Launch Live Mode</p>
            </li>
          
          </ul>

    </div>
    -->
    <div class="flex-auto">
<h3 class="text-2xl font-bold">Your Lessons</h3>
<ul role="list" class="space-y-3">
    {#each lessons as l}
    <li class="overflow-hidden rounded-md bg-white px-6 py-4 shadow">
        <p>{l.name}</p>
        <a href={`/app/${$page.params.org}/class/${$page.params.classid}/lesson/${l.id}`}>View</a>
    </li>
    {/each}
    </div>
    <div class="flex-auto">
        <h3 class="text-2xl font-bold">Your Students</h3>
    </div>
</div>