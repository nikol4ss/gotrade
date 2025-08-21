<script setup lang="ts">
import { Icon } from '@iconify/vue'
import { useColorMode } from '@vueuse/core'

const mode = useColorMode()

function toggleTheme() {
  if (mode.value === 'light') mode.value = 'dark'
  else if (mode.value === 'dark') mode.value = 'light'
  else mode.value = 'light' 
}
</script>

<template>
  <button @click="toggleTheme" class="p-1 rounded-full cursor-pointer">
    <Icon
      v-if="mode === 'dark'"
      icon="radix-icons:sun"
      class="h-4 w-4"
    />
    <Icon
      v-else
      icon="radix-icons:moon"
      class="h-4 w-4"
    />
  </button>
</template>
