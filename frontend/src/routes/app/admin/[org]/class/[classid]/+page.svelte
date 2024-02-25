<script>
    import Button from "$lib/components/generic/Button.svelte";
import PageTitle from "$lib/components/generic/PageTitle.svelte";

</script>
<PageTitle>
    <span slot="title">2024 RITSEC</span>
    <span slot="subtitle"><span class="font-light">Join Code:</span> ritsec24</span>
    <span slot="actions"><Button>New Lesson</Button></span>
</PageTitle>
<div class="flex flex-col md:flex-row">
    <div class="flex-auto">
        <h3 class="text-2xl font-bold">Today</h3>
        <ul role="list" class="space-y-3">
            <li class="overflow-hidden rounded-md bg-white px-6 py-4 shadow">
              <p>Launch Live Mode</p>
            </li>
          
          </ul>

    </div>
    <div class="flex-auto">
<h3 class="text-2xl font-bold">Your Lessons</h3>
    </div>
    <div class="flex-auto">
        <h3 class="text-2xl font-bold">Your Students</h3>
    </div>
</div>