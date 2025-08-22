<script setup lang="ts">
import { BarChart as BaseBarChart } from "@/components/ui/chart-bar"
import { type PropType } from "vue"

interface ChartData {
  name: string
  [key: string]: number | string
}

const props = defineProps({
  data: { type: Array as PropType<ChartData[]>, required: true },
  categories: { type: Array as PropType<string[]>, required: true },
  colors: { type: Array as PropType<string[]>, default: () => ['blue', 'pink', 'orange', 'red'] },
  yFormatter: {
    type: Function as PropType<(tick: number | Date, i: number, ticks: (number | Date)[]) => string>,
    default: undefined
  }
})
</script>

<template>
  <BaseBarChart
    :data="props.data"
    index="name"
    :categories="props.categories"
    :colors="props.colors"
    :y-formatter="props.yFormatter"
  />
</template>
