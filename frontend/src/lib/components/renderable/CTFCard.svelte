<script>
    import Button from "../generic/Button.svelte";
    import LottieOverlay from "../generic/LottieOverlay.svelte";
    import CardTemplate from "./CardTemplate.svelte";
    let showWin = false;
    /**
     * @property mode {('view'|'edit')}
     */
    export var mode = "view";

    export var config = {
        "title":"Unknown Flag",
        "description":"Description",
        "flag":"RS{TEST}"
    };

    function submitFlag() {
        showWin = true;
    }
</script>

<CardTemplate>
    {#if mode=="edit"}
    <input class="text-2xl font-bold w-full" placeholder="title" bind:value={config["title"]} />
    {:else}
    <h2 class="text-2xl font-bold">{config["title"]}</h2>
    {/if}

    {#if mode=="edit"}
    <textarea rows="5" class="w-full" placeholder="description" bind:value={config["description"]} />

    {:else}
    <p>{config["description"]}</p>

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
                placeholder="FLAG{1234}"
                bind:value={config["flag"]}
            />
            <br />
            
        </div>
    </div>
    {:else}
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
                placeholder="FLAG{1234}"
            />
            <br />
            <Button callback={submitFlag}>Submit</Button>
            <LottieOverlay
                bind:visible={showWin}
                url="/lottie/confetti2.json"
            />
        </div>
    </div>
    {/if}
</CardTemplate>
