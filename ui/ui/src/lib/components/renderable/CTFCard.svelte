<script>
    import Button from "../generic/Button.svelte";
import CardTemplate from "./CardTemplate.svelte";


</script>
<CardTemplate>
    <h2>Easy 1</h2>
    <p>Paragraph</p>
    <div>
        <label for="flag" class="block text-sm font-medium leading-6 text-gray-900">Enter the flag</label> <span class="inline-flex items-center rounded-md bg-gray-50 px-2 py-1 text-xs font-medium text-gray-600 ring-1 ring-inset ring-gray-500/10">Badge</span>
        <div class="mt-2">
          <input type="text" name="flag" id="flag" class="block w-full rounded-md border-0  text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6 p-2" placeholder="FLAG{1234}">
          <br />
<Button>Submit</Button>
        </div>
      </div>
</CardTemplate>