<script>
import NavBarTextIcon from "../../../lib/components/sidebar/NavBarTextIcon.svelte";
import SidebarItem from "../../../lib/components/sidebar/SidebarItem.svelte";

</script>
<div
    class="flex grow flex-col gap-y-5 overflow-y-auto bg-gray-900 px-6 pb-2 ring-1 ring-white/10"
>
    <div class="flex h-16 shrink-0 items-center">
        <img
            class="h-8 w-auto"
            src="https://tailwindui.com/img/logos/mark.svg?color=indigo&shade=500"
            alt="Your Company"
        />
        <span class="h-8 inline-flex items-center text-white px-2 font-brand leading-1">Club Name</span>
    </div>
    <nav class="flex flex-1 flex-col">
        <ul role="list" class="flex flex-1 flex-col gap-y-7">
            <li>
                <ul role="list" class="-mx-2 space-y-1">
                    <SidebarItem url="/app/learn" title="Home">
                        <ion-icon name="home-outline" slot="icon" class="hydrated"></ion-icon>
                    </SidebarItem>
                    <SidebarItem url="/app/learn" title="Classes">
                        <ion-icon name="school-outline" slot="icon" class="hydrated"> </ion-icon>
                    </SidebarItem>

                </ul>
            </li>
            <li>
                <div class="text-xs font-semibold leading-6 text-gray-400">
                    Your teams
                </div>
                <ul role="list" class="-mx-2 mt-2 space-y-1">
                    <SidebarItem url="/app/learn" title="Team 1">
                        <NavBarTextIcon char="1" slot="icon"/>
                    </SidebarItem>
                </ul>
            </li>
        </ul>
    </nav>
</div>
