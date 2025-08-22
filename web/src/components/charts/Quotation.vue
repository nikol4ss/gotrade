<!-- src/components/ui/MyTable.vue -->
<script setup lang="ts">
import {
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from "@/components/ui/table"
import { type PropType } from "vue"

interface TableRowData {
  [key: string]: string | number
}

interface Column {
  key: string
  label: string
  align?: "left" | "center" | "right"
}

const props = defineProps({
  data: { type: Array as PropType<TableRowData[]>, required: true },
  columns: { type: Array as PropType<Column[]>, required: true },
})
</script>

<template>
  <Table>
    <TableHeader>
      <TableRow>
        <TableHead v-for="col in props.columns" :key="col.key" :class="col.align === 'right' ? 'text-right' : ''">
          {{ col.label }}
        </TableHead>
      </TableRow>
    </TableHeader>
    <TableBody>
      <TableRow v-for="row in props.data" :key="row[props.columns[0].key]">
        <TableCell
          v-for="col in props.columns"
          :key="col.key"
          :class="col.align === 'right' ? 'text-right font-medium' : 'font-medium'"
        >
          {{ row[col.key] }}
        </TableCell>
      </TableRow>
    </TableBody>
  </Table>
</template>
