<script lang="ts">
    import * as api from "$lib/api";
    import { onMount } from "svelte";
    import Button from "../generic/Button.svelte";
    import LottieOverlay from "../generic/LottieOverlay.svelte";
    import CardTemplate from "./CardTemplate.svelte";
    let showWin = false;
    /**
     * @property mode {('view'|'edit')}
     */
    export var mode = "view";
    export var classId: string = "";
    export var lessonId: string = "";

    var flagValue = "";
    

    export var config: any = {"uuid":""};
    var ctfConf = {
        "title":"Unknown Flag",
        "description":"Description",
        "flag":"RS{TEST}",
        "points":10
    };

    export var obj: api.Flag = {
        id: config["uuid"],
        name: ctfConf["title"],
        config: JSON.stringify(ctfConf),
        points: ctfConf["points"]??10
    };
   
    function submitFlag() {
        if (flagValue == ctfConf["flag"]){
            showWin = true;
        }
        
    }
    async function loadCTFData() {
        api.getFlagById(classId, lessonId, config["uuid"]).then((res) => {
            if(res == null){
                return;
            }
            obj = res;
            ctfConf = JSON.parse(res.config??"{}");
        });
    }
    onMount(() => {
        loadCTFData();
    });

    function onStateUpdate(){
        if (mode == "edit"){
            obj.config = JSON.stringify(ctfConf);
            obj.points = ctfConf["points"];

            api.updateFlag(classId, lessonId, config["uuid"], obj);
        }
    }
    //$: config, ctfConf, onStateUpdate();
 

</script>

<CardTemplate>
    {#if mode=="edit"}
    <input class="text-2xl font-bold w-full" placeholder="title" bind:value={ctfConf["title"]} />
    {:else}
    <h2 class="text-2xl font-bold">{ctfConf["title"]}</h2>
    {/if}

    {#if mode=="edit"}
    <textarea rows="5" class="w-full" placeholder="description" bind:value={ctfConf["description"]} />

    {:else}
    <p>{ctfConf["description"]}</p>

    {/if}
    {#if mode == "edit"}
    <div>
        <label
            for="flag"
            class="block text-sm font-medium leading-6 text-gray-900"
            >Enter the flag</label
        >
        
        <div class="mt-2">
            <input
                type="text"
                name="flag"
                id="flag"
                class="block w-full rounded-md border-0 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-orange-600 sm:text-sm sm:leading-6 p-2"
                placeholder="FLAG&lcub;1234&rcub;"
                bind:value={ctfConf["flag"]}
            />
            <br />
            
        </div>
        <div class="mt-2">
            <input
                type="number"
                name="points"
                id="points"
                class="block w-full rounded-md border-0 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-orange-600 sm:text-sm sm:leading-6 p-2"
                placeholder="100"
                bind:value={ctfConf["points"]}
            />
            <br />
            
        </div>
        <Button callback={onStateUpdate}>Save</Button>
    </div>
    {:else}
    <div class="py-4">
        <label
            for="flag"
            class="block text-sm font-medium leading-6 text-gray-900"
            >Enter the flag</label
        >
        
        <div class="mt-2">
            <input
                type="text"
                name="flag"
                id="flag"
                class="block w-full rounded-md border-0 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-orange-600 sm:text-sm sm:leading-6 p-2"
                placeholder="FLAG&lcub;1234&rcub;"
                bind:value={flagValue}
            />
      
            <p class="text-sm text-gray-700 pb-1 pt-3">Value: {ctfConf["points"]} points</p>
            
            <Button callback={submitFlag}>Submit</Button>
            <LottieOverlay
                bind:visible={showWin}
                url="/lottie/confetti2.json"
            />
        </div>
    </div>
    {/if}
</CardTemplate>
