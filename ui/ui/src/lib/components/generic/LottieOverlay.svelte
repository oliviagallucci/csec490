<script>
     import { LottiePlayer } from '@lottiefiles/svelte-lottie-player';
    import { onMount, tick } from "svelte";

    let lottiePlayer;
    export var visible = false;
    export var url = "";
    let pageWidth, pageHeight = 0;
    $: {
        if (visible) {
            launchVisible();
        }
    }

    async function launchVisible() {
        await tick();
        const lottie = lottiePlayer.getLottie();
		lottie.addEventListener("complete", () => {
			visible = false;
		});
    }

</script>


{#if visible}
<div class="absolute self-center top-0 z-50 h-full overflow-hidden" bind:clientWidth={pageWidth} bind:clientHeight={pageHeight}>
    <LottiePlayer src={url} autoplay="true" width="{pageWidth}" height="{pageHeight}" controls="{false}" renderer="svg" background="transparent" bind:this={lottiePlayer}/>
</div>
{/if}
