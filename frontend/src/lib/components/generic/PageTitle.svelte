<div class="md:flex md:items-center md:justify-between mb-10">
    <div class="min-w-0 flex-1">
      <h2 class="text-2xl font-header leading-7 text-gray-900 sm:truncate sm:text-3xl sm:tracking-tight"><slot name="title"></slot></h2>
      <p class="text-l font-header leading-7 text-gray-900 sm:text-xl sm:tracking-light font-bold"><slot name="subtitle"></slot></p>
    </div>
    <div class="mt-4 flex md:ml-4 md:mt-0">
      <slot name="actions"></slot>
  
    </div>
  </div>