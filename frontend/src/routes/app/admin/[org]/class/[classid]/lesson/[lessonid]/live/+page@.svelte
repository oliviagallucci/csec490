<script lang="ts">
    import "../../../../../../../../../app.css";
    export const ssr = false;
    import {onMount} from "svelte";

    var selectedScreen = "rankings"

    var scores = [
        {name: "Alice", score: 0},
        {name: "Bob", score: 0},
        {name: "Charlie", score: 0},
        {name: "David", score: 0},
        {name: "Eve", score: 0},
        {name: "Frank", score: 0},
        {name: "Grace", score: 0},
        {name: "Heidi", score: 0},
        {name: "Ivan", score: 0},
        {name: "Judy", score: 0},
        {name: "Kevin", score: 0},
    
    ];
    var oldScores = []

    function updateRandomScores(){
        oldScores.push(scores)
        let randomId = Math.floor(Math.random() * scores.length);
        scores[randomId].score = Math.floor(Math.random() * 100);
    }
    function simulateSetting(){
        setInterval(updateRandomScores, 1000);
    
    }
    onMount(()=>{
        simulateSetting();
    });
    
</script>
<div class="w-full h-full absolute top-0 left-0">
    {#if selectedScreen == "rankings"}
    {#each scores as s}
    <div class="w-full h-16 flex justify-between items-center px-4">
        <p>{s.name}</p>
        <p>{s.score}</p>
    </div>
        
    {/each}
    {:else if selectedScreen == "trends"}
    <div class="w-full h-full flex justify-center items-center">
        <p>Coming Soon</p>
    </div>

{/if}
</div>
