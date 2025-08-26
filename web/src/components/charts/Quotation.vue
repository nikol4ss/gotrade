<script setup lang="ts">
import {
  Table,
  TableBody,
  TableCaption,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from "@/components/ui/table"
import type { PropType } from "vue"

interface Column {
  key: string
  label: string
  align?: "left" | "center" | "right"
  icon?: any
}

defineProps({
  caption: { type: String, default: "" },
  data: { type: Array as PropType<Record<string, any>[]>, required: true },
  columns: { type: Array as PropType<Column[]>, required: true },
})

function parseNumber(value: string | number) {
  if (typeof value === 'number') return value
  if (!value) return 0
  return parseFloat(value.replace(/[$,%]/g, '').replace(/,/g, '')) || 0
}
</script>

<template>
  <Table>
    <TableCaption v-if="caption">{{ caption }}</TableCaption>

    <TableHeader>
      <TableRow>
        <TableHead v-for="col in columns" :key="col.key"
          :class="col.align === 'center' ? 'text-center' : col.align === 'right' ? 'text-right' : 'text-left'">
          <span class="flex items-center gap-1">
            {{ col.label }}
            <component v-if="col.icon" :is="col.icon" class="w-3 h-3 text-gray-500" />
          </span>
        </TableHead>
      </TableRow>
    </TableHeader>

    <TableBody>
      <TableRow v-for="(row, i) in data" :key="i">
        <TableCell v-for="col in columns" :key="col.key"
          :class="col.align === 'center' ? 'text-center font-medium' : col.align === 'right' ? 'text-right font-medium' : 'text-left font-medium'">

          <template v-if="col.key === 'display_name'">
            <span class="flex items-center gap-2">
              <img v-if="row.logo" :src="row.logo" :alt="row.display_name" class="w-5 h-5 rounded-full" />
              <span class="font-bold">{{ row.display_name.split(' - ')[0] }}</span>
              <span class="text-xs text-muted-foreground">{{ row.display_name.split(' - ')[1] }}</span>
            </span>
          </template>

          <template v-else-if="col.key === 'price_change_percentage_24h' || col.key === 'price_change_24h'">
            <span :class="parseNumber(row[col.key]) > 0
              ? 'text-green-800 inline-flex items-center gap-2'
              : parseNumber(row[col.key]) < 0
                ? 'text-red-800 inline-flex items-center gap-1'
                : 'text-muted-foreground inline-flex items-center gap-2'">
              <svg v-if="parseNumber(row[col.key]) > 0" class="w-3 h-3" fill="currentColor" viewBox="0 0 20 20">
                <path d="M10 5l5 5H5l5-5z" />
              </svg>
              <svg v-else-if="parseNumber(row[col.key]) < 0" class="w-3 h-3" fill="currentColor" viewBox="0 0 20 20">
                <path d="M10 15l-5-5h10l-5 5z" />
              </svg>
              <svg v-else class="w-3 h-3" fill="currentColor" viewBox="0 0 20 20">
                <circle cx="10" cy="10" r="3" />
              </svg>

              {{ row[col.key].replace('$-0.00', '$0.00').replace('-0.00%', '0.00%') }}
            </span>
          </template>

          <template v-else>
            {{ row[col.key] }}
          </template>

        </TableCell>
      </TableRow>
    </TableBody>
  </Table>
</template>
