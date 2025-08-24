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
  colors: {
    type: Array as PropType<string[]>,
    default: () => [
      '#1E293B',
      '#475569',
      '#64748B',
      '#94A3B8',
      '#F1F5F9'
    ]
  },
  valueFormatter: {
    type: Function as PropType<(tick: number | Date, i?: number, ticks?: (number | Date)[]) => string>,
    default: undefined
  },
  type: {
    type: String as PropType<"donut" | "pie">,
    default: "donut"
  },
})

</script>

<template>
  <BaseDonutChart index="name" :data="props.data" :category="props.category" :colors="props.colors"
    :value-formatter="props.valueFormatter" :type="props.type" />
</template>
