<script setup lang="ts">
import { DonutChart as BaseDonutChart } from "@/components/ui/chart-donut"
import { type PropType } from "vue"

interface ChartData {
  name: string
  [key: string]: number | string
}

const props = defineProps({
  data: { type: Array as PropType<ChartData[]>, required: true },
  category: { type: String, required: true },
  colors: { type: Array as PropType<string[]>, default: () => ['blue','pink','orange','red'] },
  valueFormatter: {
    type: Function as PropType<(tick: number | Date, i?: number, ticks?: (number | Date)[]) => string>,
    default: undefined
  }
})
</script>

<template>
  <BaseDonutChart
    :data="props.data"
    :category="props.category"
    :colors="props.colors"
    :value-formatter="props.valueFormatter"
    index="name"
  />
</template>
