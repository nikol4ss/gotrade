<script setup lang="ts">
import { LineChart as BaseLineChart } from "@/components/ui/chart-line"
import { type PropType } from "vue"

interface ChartData {
  [key: string]: number | string
}

const props = defineProps({
  data: { type: Array as PropType<ChartData[]>, required: true },
  categories: { type: Array as PropType<string[]>, required: true },
  colors: {
    type: Array as PropType<string[]>, default: () => ['yellow'] },
  yFormatter: {
        type: Function as PropType<(tick: number | Date, i?: number, ticks?: (number | Date)[]) => string>,
        default: undefined
      }
})
</script>

<template>
  <BaseLineChart :data="props.data" index="year" :categories="props.categories" :colors="props.colors"
    :y-formatter="props.yFormatter" />
</template>
