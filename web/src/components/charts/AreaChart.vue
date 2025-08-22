<script setup lang="ts">
import { AreaChart as BaseAreaChart } from "@/components/ui/chart-area"
import { type PropType } from "vue"

interface ChartData {
  name: string
  [key: string]: number | string
}

const props = defineProps({
  data: { type: Array as PropType<ChartData[]>, required: true },
  categories: { type: Array as PropType<string[]>, required: true },
  colors: { type: Array as PropType<string[]>, default: () => ['blue', 'pink', 'orange', 'red'] }
})
</script>

<template>
  <BaseAreaChart :data="props.data" index="name" :categories="props.categories" :colors="props.colors" />
</template>
