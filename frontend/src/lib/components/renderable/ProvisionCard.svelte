<script>
    import { fade } from "svelte/transition";
    import Button from "../generic/Button.svelte";
import CardTemplate from "./CardTemplate.svelte";
    import Progress from "../generic/Progress.svelte";
    /**
     * @typedef {number} VMState*/
    
    const VMSTATE = {
        NONE: 1,
        LOADING: 2,
        ACTIVE: 3,
        SHUTDOWN: 4,
        ERROR: 4
    }
    const TRANSITION_DURATION = 150;
    var loadPercentage = 0;
    var vmState = VMSTATE.NONE;

    function loadVM(){
        vmState = VMSTATE.LOADING;
        loadPercentage = 0;

        var interval = setInterval(function(){
            loadPercentage += 10;
            if(loadPercentage >= 100){
                clearInterval(interval);
                loadPercentage = 0;
                vmState = VMSTATE.ACTIVE;
            }
        }, 500);
    
    }
    function connectToVM(){
        alert("Connected to VM");
    }
    function stopVM(){
        vmState = VMSTATE.SHUTDOWN;
        loadPercentage = 0;
        var interval = setInterval(function(){
            loadPercentage += 10;
            if(loadPercentage >= 100){
                clearInterval(interval);
                loadPercentage = 0;
                vmState = VMSTATE.NONE;
            }
        }, 500);
    }
    /**
     * @property mode {('view'|'edit')}
     */
    export var mode = "view";
    export var config = {
        "image":""
    }
</script>
<CardTemplate>
    {#if mode == "edit"}
    <input
                type="text"
                name="vmURL"
                id="vmURL"
                class="block w-full rounded-md border-0 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-orange-600 sm:text-sm sm:leading-6 p-2"
                placeholder="VM URL"
                bind:value={config["image"]}
            />
    {:else}
    <h2>VM Name</h2>
    {#if vmState === VMSTATE.NONE}
    <div out:fade={{duration: TRANSITION_DURATION}} in:fade={{duration: TRANSITION_DURATION, delay: TRANSITION_DURATION}}>
        <Button callback={()=>{loadVM();}}>Start VM</Button>

    </div>
    {:else if vmState === VMSTATE.LOADING}
    <div out:fade={{duration: TRANSITION_DURATION}} in:fade={{duration: TRANSITION_DURATION, delay: TRANSITION_DURATION}}>
        <Progress value={loadPercentage} />
    </div>
    
    {:else if vmState === VMSTATE.ACTIVE}
    <div out:fade={{duration: TRANSITION_DURATION}} in:fade={{duration: TRANSITION_DURATION, delay: TRANSITION_DURATION}}>
        <span class="inline-flex items-center rounded-md bg-green-50 px-2 py-1 text-xs font-medium text-green-700 ring-1 ring-inset ring-green-600/20">Online</span>
        <br />
    
          <Button callback={()=>{connectToVM();}}>Connect</Button>
          <Button callback={()=>{stopVM()}}>Stop</Button>
    </div>
    {:else if vmState === VMSTATE.SHUTDOWN}
    <div out:fade={{duration: TRANSITION_DURATION}} in:fade={{duration: TRANSITION_DURATION, delay: TRANSITION_DURATION}}>
        <p>Shutting Down VM</p>
        <Progress value={loadPercentage} />
    </div>
    {:else if vmState === VMSTATE.ERROR}
    <p>There was an error</p>
    {/if}
    {/if}
</CardTemplate>