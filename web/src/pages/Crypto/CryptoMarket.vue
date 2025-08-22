<script setup lang="ts">
import { DollarSign, PieChart, TrendingUp, Activity, AlertCircle, CreditCard, BookOpen, Star } from 'lucide-vue-next';
import AreaChart from '@/components/charts/AreaChart.vue';
import LineChart from '@/components/charts/LineChart.vue';
import DonutChart from '@/components/charts/DonutChart.vue';
import Quotation from '@/components/charts/Quotation.vue';

const revenueData = [
  { name: "Jan", total: 1000, predicted: 1200 },
  { name: "Feb", total: 1100, predicted: 1300 },
];

const portfolioData = [
  { name: "BTC", value: 40 },
  { name: "ETH", value: 25 },
  { name: "ADA", value: 20 },
  { name: "SOL", value: 15 },
];

const quotationData = [
  { name: "BTC", price: 30000 },
  { name: "ETH", price: 2000 },
];

const yFormatter = (tick: number | Date, _i?: number, _ticks?: (number | Date)[]) => {
  if (typeof tick === "number") return `$ ${new Intl.NumberFormat("us").format(tick)}`;
  return tick.toString();
};

const valueFormatter = (tick: number | Date) => {
  if (typeof tick === "number") return `$ ${new Intl.NumberFormat("us").format(tick)}`;
  return tick.toString();
};
</script>

<template>
  <div class="flex flex-1 flex-col gap-6 p-4">

    <!-- Linha 1: Cotações e Distribuição -->
    <div class="grid gap-4 md:grid-cols-2">
      <div class="rounded-xl bg-muted/50 p-4 flex flex-col h-full">
        <div class="flex items-center gap-2 mb-2"><DollarSign class="w-5 h-5" /><h2 class="text-lg font-semibold">Cotações</h2></div>
        <!-- <Quotation :data="quotationData" class="flex-1 w-full h-72 md:h-96" /> -->
      </div>

      <div class="rounded-xl bg-muted/50 p-4 flex flex-col h-full">
        <div class="flex items-center gap-2 mb-2"><PieChart class="w-5 h-5" /><h2 class="text-lg font-semibold">Distribuição de Criptomoedas</h2></div>
        <DonutChart :data="portfolioData" category="value" :value-formatter="valueFormatter" class="flex-1 w-full h-72 md:h-96" />
      </div>
    </div>

    <!-- Linha 2: Histórico de preços -->
    <div class="rounded-xl bg-muted/50 p-4 flex flex-col h-full">
      <div class="flex items-center gap-2 mb-2"><TrendingUp class="w-5 h-5" /><h2 class="text-lg font-semibold">Histórico de Preços</h2></div>
      <AreaChart :data="revenueData" :categories="['total','predicted']" :colors="['blue','green']" :y-formatter="yFormatter" class="flex-1 w-full h-72 md:h-96" />
    </div>

    <!-- Linha 3: Indicadores e Volume -->
    <div class="grid gap-4 md:grid-cols-2">
      <div class="rounded-xl bg-muted/50 p-4 flex flex-col items-center justify-center h-full">
        <div class="flex items-center gap-2 mb-2"><Activity class="w-5 h-5" /><h2 class="text-lg font-semibold">Indicadores Técnicos</h2></div>
        <span class="text-muted-foreground">RSI, MACD, SMA, Bollinger Bands...</span>
      </div>

      <div class="rounded-xl bg-muted/50 p-4 flex flex-col items-center justify-center h-full">
        <div class="flex items-center gap-2 mb-2"><Star class="w-5 h-5" /><h2 class="text-lg font-semibold">Volume e Market Cap</h2></div>
        <span class="text-muted-foreground">Volume 24h, Market Cap, Dominância BTC/ETH...</span>
      </div>
    </div>

    <!-- Linha 4: Tendência de preços e alertas -->
    <div class="grid gap-4 md:grid-cols-2">
      <div class="rounded-xl bg-muted/50 p-4 flex flex-col h-full">
        <div class="flex items-center gap-2 mb-2"><TrendingUp class="w-5 h-5" /><h2 class="text-lg font-semibold">Tendência de Preços</h2></div>
        <LineChart :data="revenueData" :categories="['total','predicted']" :colors="['blue','green']" :y-formatter="yFormatter" class="flex-1 w-full h-72 md:h-96" />
      </div>

      <div class="rounded-xl bg-muted/50 p-4 flex flex-col items-center justify-center h-full">
        <div class="flex items-center gap-2 mb-2"><AlertCircle class="w-5 h-5" /><h2 class="text-lg font-semibold">Alertas Preventivos</h2></div>
        <span class="text-muted-foreground">Sinais de sobrecompra/sobrevenda, volatilidade alta...</span>
      </div>
    </div>

    <!-- Linha 5: Conversor e Notícias -->
    <div class="grid gap-4 md:grid-cols-2">
      <div class="rounded-xl bg-muted/50 p-4 flex flex-col items-center justify-center h-full">
        <div class="flex items-center gap-2 mb-2"><CreditCard class="w-5 h-5" /><h2 class="text-lg font-semibold">Conversor de Criptomoedas</h2></div>
        <span class="text-muted-foreground">BTC ↔ USD, ETH ↔ BTC, etc.</span>
      </div>

      <div class="rounded-xl bg-muted/50 p-4 flex flex-col items-center justify-center h-full">
        <div class="flex items-center gap-2 mb-2"><BookOpen class="w-5 h-5" /><h2 class="text-lg font-semibold">Notícias do Mercado</h2></div>
        <span class="text-muted-foreground">Últimas notícias e análises de criptomoedas</span>
      </div>
    </div>
  </div>
</template>
