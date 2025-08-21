<script setup lang="ts">
import { DollarSign, PieChart, TrendingUp, Activity, AlertCircle, CreditCard, BookOpen, Star } from 'lucide-vue-next';
import Quotation from '@/components/charts/Quotation.vue';
import AreaChart from '@/components/charts/AreaChart.vue';
import DonutChart from '@/components/charts/DonutChart.vue';
import LineChart from '@/components/charts/LineChart.vue';
</script>

<template>
  <div class="flex flex-1 flex-col gap-6 p-4">

    <div class="grid gap-4 md:grid-cols-2">
      <div class="rounded-xl bg-muted/50 p-4 flex flex-col h-full">
        <div class="flex items-center gap-2 mb-2">
          <DollarSign class="w-5 h-5"/>
          <h2 class="text-lg font-semibold">Cotações</h2>
        </div>
        <Quotation class="flex-1 w-full h-full" />
      </div>
      <div class="rounded-xl bg-muted/50 p-4 flex flex-col h-full">
        <div class="flex items-center gap-2 mb-2">
          <PieChart class="w-5 h-5"/>
          <h2 class="text-lg font-semibold">Distribuição de Criptomoedas</h2>
        </div>
        <DonutChart class="flex-1 w-full h-full" />
      </div>
    </div>

    <div class="rounded-xl bg-muted/50 p-4 flex flex-col h-full">
      <div class="flex items-center gap-2 mb-2">
        <TrendingUp class="w-5 h-5"/>
        <h2 class="text-lg font-semibold">Histórico de Preços</h2>
      </div>
      <AreaChart class="flex-1 w-full h-full" />
    </div>

    <div class="grid gap-4 md:grid-cols-2">
      <div class="rounded-xl bg-muted/50 p-4 flex flex-col items-center justify-center h-full">
        <div class="flex items-center gap-2 mb-2">
          <Activity class="w-5 h-5"/>
          <h2 class="text-lg font-semibold">Indicadores Técnicos</h2>
        </div>
        <span class="text-muted-foreground">RSI, MACD, SMA, Bollinger Bands...</span>
      </div>
      <div class="rounded-xl bg-muted/50 p-4 flex flex-col items-center justify-center h-full">
        <div class="flex items-center gap-2 mb-2">
          <Star class="w-5 h-5"/>
          <h2 class="text-lg font-semibold">Volume e Market Cap</h2>
        </div>
        <span class="text-muted-foreground">Volume 24h, Market Cap, Dominância BTC/ETH...</span>
      </div>
    </div>

    <div class="grid gap-4 md:grid-cols-2">
      <div class="rounded-xl bg-muted/50 p-4 flex flex-col h-full">
        <div class="flex items-center gap-2 mb-2">
          <TrendingUp class="w-5 h-5"/>
          <h2 class="text-lg font-semibold">Tendência de Preços</h2>
        </div>
        <LineChart class="flex-1 w-full h-full" />
      </div>
      <div class="rounded-xl bg-muted/50 p-4 flex flex-col items-center justify-center h-full">
        <div class="flex items-center gap-2 mb-2">
          <AlertCircle class="w-5 h-5"/>
          <h2 class="text-lg font-semibold">Alertas Preventivos</h2>
        </div>
        <span class="text-muted-foreground">Sinais de sobrecompra/sobrevenda, volatilidade alta...</span>
      </div>
    </div>

    <div class="grid gap-4 md:grid-cols-2">
      <div class="rounded-xl bg-muted/50 p-4 flex flex-col items-center justify-center h-full">
        <div class="flex items-center gap-2 mb-2">
          <CreditCard class="w-5 h-5"/>
          <h2 class="text-lg font-semibold">Conversor de Criptomoedas</h2>
        </div>
        <span class="text-muted-foreground">BTC ↔ USD, ETH ↔ BTC, etc.</span>
      </div>
      <div class="rounded-xl bg-muted/50 p-4 flex flex-col items-center justify-center h-full">
        <div class="flex items-center gap-2 mb-2">
          <BookOpen class="w-5 h-5"/>
          <h2 class="text-lg font-semibold">Notícias do Mercado</h2>
        </div>
        <span class="text-muted-foreground">Últimas notícias e análises de criptomoedas</span>
      </div>
    </div>

    <div class="grid gap-4 md:grid-cols-2">
      <div class="rounded-xl bg-muted/50 p-4 flex flex-col h-full">
        <div class="flex items-center gap-2 mb-2">
          <Star class="w-5 h-5"/>
          <h2 class="text-lg font-semibold">Top Criptomoedas</h2>
        </div>
        <span class="text-muted-foreground">Mais valorizadas, mais negociadas</span>
      </div>
      <div class="rounded-xl bg-muted/50 p-4 flex flex-col h-full">
        <div class="flex items-center gap-2 mb-2">
          <PieChart class="w-5 h-5"/>
          <h2 class="text-lg font-semibold">Carteira Simulada</h2>
        </div>
        <span class="text-muted-foreground">Visualização de performance hipotética</span>
      </div>
    </div>

    <div class="grid gap-4 md:grid-cols-2">
      <div class="rounded-xl bg-muted/50 p-4 flex flex-col h-full">
        <div class="flex items-center gap-2 mb-2">
          <DollarSign class="w-5 h-5"/>
          <h2 class="text-lg font-semibold">Dominância de Mercado</h2>
        </div>
        <span class="text-muted-foreground">BTC, ETH e outras altcoins</span>
      </div>
      <div class="rounded-xl bg-muted/50 p-4 flex flex-col h-full">
        <div class="flex items-center gap-2 mb-2">
          <TrendingUp class="w-5 h-5"/>
          <h2 class="text-lg font-semibold">Tendência Geral do Mercado</h2>
        </div>
        <span class="text-muted-foreground">Indicadores agregados, volatilidade, sentimento</span>
      </div>
    </div>

    <div class="rounded-xl bg-muted/50 p-4 flex flex-col h-64">
      <div class="flex items-center gap-2 mb-2">
        <AlertCircle class="w-5 h-5"/>
        <h2 class="text-lg font-semibold">Feedback e Recomendações</h2>
      </div>
      <div class="flex-1 rounded-xl bg-muted/30 flex items-center justify-center">
        <span class="text-muted-foreground">Sugestões de ajuste baseadas em indicadores e tendências</span>
      </div>
    </div>

  </div>
</template>
