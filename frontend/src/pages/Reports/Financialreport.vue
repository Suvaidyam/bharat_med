<template>
	<div class="min-h-screen bg-gray-50 p-4 md:p-6">
		<!-- Header -->
		<div class="mb-8">
			<div class="flex flex-col md:flex-row md:items-center md:justify-between gap-4">
				<div>
					<h1 class="text-2xl md:text-3xl font-bold text-gray-900">Financial Reports</h1>
					<p class="text-gray-600 mt-1">
						Track revenue, expenses, and financial performance metrics
					</p>
				</div>

				<!-- Controls -->
				<div class="flex flex-wrap items-center gap-3">
					<div class="flex items-center gap-2 bg-white px-3 py-2 rounded-lg border">
						<svg
							class="w-4 h-4 text-gray-500"
							fill="none"
							stroke="currentColor"
							viewBox="0 0 24 24"
						>
							<path
								stroke-linecap="round"
								stroke-linejoin="round"
								stroke-width="2"
								d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"
							/>
						</svg>
						<span class="text-sm text-gray-700">{{ selectedDateRange }}</span>
					</div>

					<select
						v-model="selectedDepartment"
						class="bg-white px-3 py-2 rounded-lg border text-sm"
					>
						<option value="all">All Departments</option>
						<option value="cardiology">Cardiology</option>
						<option value="orthopedics">Orthopedics</option>
						<option value="neurology">Neurology</option>
					</select>

					<select
						v-model="selectedService"
						class="bg-white px-3 py-2 rounded-lg border text-sm"
					>
						<option value="all">All Services</option>
						<option value="consultation">Consultation</option>
						<option value="surgery">Surgery</option>
						<option value="therapy">Therapy</option>
					</select>

					<button
						class="flex items-center gap-2 bg-white px-3 py-2 rounded-lg border hover:bg-gray-50"
					>
						<svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
							<path
								stroke-linecap="round"
								stroke-linejoin="round"
								stroke-width="2"
								d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15"
							/>
						</svg>
						<span class="text-sm">Refresh</span>
					</button>

					<button
						class="flex items-center gap-2 bg-blue-600 text-white px-3 py-2 rounded-lg hover:bg-blue-700"
					>
						<svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
							<path
								stroke-linecap="round"
								stroke-linejoin="round"
								stroke-width="2"
								d="M12 10v6m0 0l-3-3m3 3l3-3m2 8H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"
							/>
						</svg>
						<span class="text-sm">Export</span>
					</button>
				</div>
			</div>
		</div>

		<!-- KPI Cards -->
		<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mb-8">
			<!-- Total Revenue -->
			<div class="bg-white p-6 rounded-xl shadow-sm border">
				<div class="flex items-center justify-between mb-4">
					<h3 class="text-sm font-medium text-gray-600">Total Revenue</h3>
					<div class="p-2 bg-green-100 rounded-lg">
						<svg
							class="w-5 h-5 text-green-600"
							fill="none"
							stroke="currentColor"
							viewBox="0 0 24 24"
						>
							<path
								stroke-linecap="round"
								stroke-linejoin="round"
								stroke-width="2"
								d="M12 8c-1.657 0-3 .895-3 2s1.343 2 3 2 3 .895 3 2-1.343 2-3 2m0-8c1.11 0 2.08.402 2.599 1M12 8V7m0 1v8m0 0v1m0-1c-1.11 0-2.08-.402-2.599-1"
							/>
						</svg>
					</div>
				</div>
				<div class="text-3xl font-bold text-gray-900 mb-2">$128,450</div>
				<div class="flex items-center text-sm">
					<span class="text-gray-500">From previous month</span>
				</div>
				<div class="w-full bg-gray-200 rounded-full h-1 mt-4">
					<div class="bg-blue-600 h-1 rounded-full" style="width: 75%"></div>
				</div>
			</div>

			<!-- Total Expenses -->
			<div class="bg-white p-6 rounded-xl shadow-sm border">
				<div class="flex items-center justify-between mb-4">
					<h3 class="text-sm font-medium text-gray-600">Total Expenses</h3>
					<div class="p-2 bg-red-100 rounded-lg">
						<svg
							class="w-5 h-5 text-red-600"
							fill="none"
							stroke="currentColor"
							viewBox="0 0 24 24"
						>
							<path
								stroke-linecap="round"
								stroke-linejoin="round"
								stroke-width="2"
								d="M9 7h6m0 10v-3m-3 3h.01M9 17h.01M9 14h.01M12 14h.01M15 11h.01M12 11h.01M9 11h.01M7 21h10a2 2 0 002-2V5a2 2 0 00-2-2H7a2 2 0 00-2 2v14a2 2 0 002 2z"
							/>
						</svg>
					</div>
				</div>
				<div class="text-3xl font-bold text-gray-900 mb-2">$87,325</div>
				<div class="flex items-center text-sm">
					<span class="text-gray-500">From previous month</span>
				</div>
				<div class="w-full bg-gray-200 rounded-full h-1 mt-4">
					<div class="bg-red-500 h-1 rounded-full" style="width: 60%"></div>
				</div>
			</div>

			<!-- Net Profit -->
			<div class="bg-white p-6 rounded-xl shadow-sm border">
				<div class="flex items-center justify-between mb-4">
					<h3 class="text-sm font-medium text-gray-600">Net Profit</h3>
					<div class="p-2 bg-green-100 rounded-lg">
						<svg
							class="w-5 h-5 text-green-600"
							fill="none"
							stroke="currentColor"
							viewBox="0 0 24 24"
						>
							<path
								stroke-linecap="round"
								stroke-linejoin="round"
								stroke-width="2"
								d="M13 7h8m0 0v8m0-8l-8 8-4-4-6 6"
							/>
						</svg>
					</div>
				</div>
				<div class="text-3xl font-bold text-gray-900 mb-2">$41,125</div>
				<div class="flex items-center text-sm">
					<span class="text-gray-500">From previous month</span>
				</div>
				<div class="w-full bg-gray-200 rounded-full h-1 mt-4">
					<div class="bg-green-500 h-1 rounded-full" style="width: 32%"></div>
				</div>
			</div>

			<!-- Outstanding Payments -->
			<div class="bg-white p-6 rounded-xl shadow-sm border">
				<div class="flex items-center justify-between mb-4">
					<h3 class="text-sm font-medium text-gray-600">Outstanding Payments</h3>
					<div class="p-2 bg-yellow-100 rounded-lg">
						<svg
							class="w-5 h-5 text-yellow-600"
							fill="none"
							stroke="currentColor"
							viewBox="0 0 24 24"
						>
							<path
								stroke-linecap="round"
								stroke-linejoin="round"
								stroke-width="2"
								d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"
							/>
						</svg>
					</div>
				</div>
				<div class="text-3xl font-bold text-gray-900 mb-2">$23,540</div>
				<div class="flex items-center text-sm">
					<span class="text-gray-500">From previous month</span>
				</div>
				<div class="w-full bg-gray-200 rounded-full h-1 mt-4">
					<div class="bg-yellow-500 h-1 rounded-full" style="width: 18%"></div>
				</div>
			</div>
		</div>

		<!-- Navigation Tabs -->
		<div class="mb-6">
			<nav class="flex space-x-8 border-b border-gray-200">
				<button
					v-for="tab in tabs"
					:key="tab.id"
					@click="activeTab = tab.id"
					:class="[
						'py-2 px-1 border-b-2 font-medium text-sm',
						activeTab === tab.id
							? 'border-blue-500 text-blue-600'
							: 'border-transparent text-gray-500 hover:text-gray-700 hover:border-gray-300',
					]"
				>
					{{ tab.name }}
				</button>
			</nav>
		</div>

		<!-- Charts Section -->
		<div class="grid grid-cols-1 lg:grid-cols-2 gap-8 mb-8">
			<!-- Revenue vs Expenses Chart -->
			<div class="bg-white p-6 rounded-xl shadow-sm border">
				<h3 class="text-lg font-semibold text-gray-900 mb-2">Revenue vs Expenses</h3>
				<p class="text-sm text-gray-600 mb-6">
					Monthly comparison of revenue and expenses
				</p>

				<!-- Chart Container -->
				<div class="h-80">
					<canvas ref="revenueChart" class="w-full h-full"></canvas>
				</div>
			</div>

			<!-- Revenue by Department Chart -->
			<div class="bg-white p-6 rounded-xl shadow-sm border">
				<h3 class="text-lg font-semibold text-gray-900 mb-2">Revenue by Department</h3>
				<p class="text-sm text-gray-600 mb-6">
					Distribution of revenue across different departments
				</p>

				<!-- Pie Chart Container -->
				<div class="h-80 flex items-center justify-center">
					<canvas ref="departmentChart" class="w-full h-full"></canvas>
				</div>
			</div>
		</div>

		<!-- Financial Summary Table -->
		<div class="bg-white rounded-xl shadow-sm border">
			<div class="p-6 border-b border-gray-200">
				<div class="flex flex-col md:flex-row md:items-center md:justify-between gap-4">
					<div>
						<h3 class="text-lg font-semibold text-gray-900">Financial Summary</h3>
						<p class="text-sm text-gray-600">Monthly financial performance metrics</p>
					</div>

					<div class="flex items-center gap-3">
						<div class="relative">
							<input
								type="text"
								placeholder="Search..."
								v-model="searchQuery"
								class="pl-10 pr-4 py-2 border border-gray-300 rounded-lg text-sm focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
							/>
							<svg
								class="absolute left-3 top-2.5 h-4 w-4 text-gray-400"
								fill="none"
								stroke="currentColor"
								viewBox="0 0 24 24"
							>
								<path
									stroke-linecap="round"
									stroke-linejoin="round"
									stroke-width="2"
									d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"
								/>
							</svg>
						</div>

						<button
							class="flex items-center gap-2 px-3 py-2 border border-gray-300 rounded-lg text-sm hover:bg-gray-50"
						>
							<svg
								class="w-4 h-4"
								fill="none"
								stroke="currentColor"
								viewBox="0 0 24 24"
							>
								<path
									stroke-linecap="round"
									stroke-linejoin="round"
									stroke-width="2"
									d="M3 4a1 1 0 011-1h16a1 1 0 011 1v2.586a1 1 0 01-.293.707l-6.414 6.414a1 1 0 00-.293.707V17l-4 4v-6.586a1 1 0 00-.293-.707L3.293 7.293A1 1 0 013 6.586V4z"
								/>
							</svg>
							Filter
						</button>
					</div>
				</div>
			</div>

			<!-- Table -->
			<div class="overflow-x-auto">
				<table class="w-full">
					<thead class="bg-gray-50">
						<tr>
							<th
								class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
							>
								Month
							</th>
							<th
								class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
							>
								Revenue
							</th>
							<th
								class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
							>
								Expenses
							</th>
							<th
								class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
							>
								Profit
							</th>
							<th
								class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
							>
								Margin
							</th>
							<th
								class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
							>
								Growth
							</th>
						</tr>
					</thead>
					<tbody class="bg-white divide-y divide-gray-200">
						<tr
							v-for="row in filteredFinancialData"
							:key="row.month"
							class="hover:bg-gray-50"
						>
							<td
								class="px-6 py-4 whitespace-nowrap text-sm font-medium text-gray-900"
							>
								{{ row.month }}
							</td>
							<td class="px-6 py-4 whitespace-nowrap text-sm text-gray-900">
								${{ row.revenue.toLocaleString() }}
							</td>
							<td class="px-6 py-4 whitespace-nowrap text-sm text-gray-900">
								${{ row.expenses.toLocaleString() }}
							</td>
							<td class="px-6 py-4 whitespace-nowrap text-sm text-gray-900">
								${{ row.profit.toLocaleString() }}
							</td>
							<td class="px-6 py-4 whitespace-nowrap text-sm text-gray-900">
								{{ row.margin }}%
							</td>
							<td class="px-6 py-4 whitespace-nowrap text-sm">
								<span
									:class="[
										'inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium',
										row.growth > 0
											? 'bg-green-100 text-green-800'
											: 'bg-red-100 text-red-800',
									]"
								>
									<svg
										v-if="row.growth > 0"
										class="w-3 h-3 mr-1"
										fill="none"
										stroke="currentColor"
										viewBox="0 0 24 24"
									>
										<path
											stroke-linecap="round"
											stroke-linejoin="round"
											stroke-width="2"
											d="M13 7h8m0 0v8m0-8l-8 8-4-4-6 6"
										/>
									</svg>
									<svg
										v-else
										class="w-3 h-3 mr-1"
										fill="none"
										stroke="currentColor"
										viewBox="0 0 24 24"
									>
										<path
											stroke-linecap="round"
											stroke-linejoin="round"
											stroke-width="2"
											d="M13 17h8m0 0V9m0 8l-8-8-4 4-6-6"
										/>
									</svg>
									{{ row.growth > 0 ? '+' : '' }}{{ row.growth }}%
								</span>
							</td>
						</tr>
					</tbody>
				</table>
			</div>
		</div>
	</div>
</template>

<script setup>
import { ref, computed, onMounted, nextTick } from 'vue'

// Reactive data
const selectedDateRange = ref('Jul 01, 2025 - Jul 01, 2025')
const selectedDepartment = ref('all')
const selectedService = ref('all')
const activeTab = ref('overview')
const searchQuery = ref('')

// Chart refs
const revenueChart = ref(null)
const departmentChart = ref(null)

// Navigation tabs
const tabs = ref([
	{ id: 'overview', name: 'Overview' },
	{ id: 'revenue', name: 'Revenue' },
	{ id: 'expenses', name: 'Expenses' },
	{ id: 'transactions', name: 'Transactions' },
])

// Financial data
const financialData = ref([
	{
		month: 'April 2025',
		revenue: 128450,
		expenses: 87325,
		profit: 41125,
		margin: 32,
		growth: 12.8,
	},
	{
		month: 'March 2025',
		revenue: 108650,
		expenses: 82850,
		profit: 25800,
		margin: 23.7,
		growth: 8.5,
	},
	{
		month: 'February 2025',
		revenue: 100150,
		expenses: 76350,
		profit: 23800,
		margin: 23.8,
		growth: -2.1,
	},
])

// Department data for pie chart
const departmentData = ref([
	{ name: 'Cardiology', value: 27, color: '#3B82F6' },
	{ name: 'Orthopedics', value: 22, color: '#10B981' },
	{ name: 'Neurology', value: 18, color: '#F59E0B' },
	{ name: 'Pediatrics', value: 17, color: '#EF4444' },
	{ name: 'Dermatology', value: 10, color: '#8B5CF6' },
	{ name: 'Other', value: 6, color: '#6B7280' },
])

// Computed properties
const filteredFinancialData = computed(() => {
	if (!searchQuery.value) return financialData.value

	return financialData.value.filter((row) =>
		row.month.toLowerCase().includes(searchQuery.value.toLowerCase()),
	)
})

// Chart initialization
const initCharts = () => {
	// Revenue vs Expenses Bar Chart (simplified representation)
	if (revenueChart.value) {
		const ctx = revenueChart.value.getContext('2d')

		// Clear canvas
		ctx.clearRect(0, 0, revenueChart.value.width, revenueChart.value.height)

		// Draw simple bar chart
		const data = [
			{ month: 'Feb', revenue: 100150, expenses: 76350 },
			{ month: 'Mar', revenue: 108650, expenses: 82850 },
			{ month: 'Apr', revenue: 128450, expenses: 87325 },
		]

		const maxValue = Math.max(...data.map((d) => Math.max(d.revenue, d.expenses)))
		const chartHeight = 200
		const chartWidth = 300
		const barWidth = 30
		const spacing = 60

		ctx.fillStyle = '#EF4444'
		data.forEach((d, i) => {
			const x = 50 + i * spacing
			const height = (d.revenue / maxValue) * chartHeight
			ctx.fillRect(x, chartHeight - height + 50, barWidth, height)
		})

		ctx.fillStyle = '#10B981'
		data.forEach((d, i) => {
			const x = 50 + i * spacing + barWidth + 5
			const height = (d.expenses / maxValue) * chartHeight
			ctx.fillRect(x, chartHeight - height + 50, barWidth, height)
		})
	}

	// Department Pie Chart (simplified representation)
	if (departmentChart.value) {
		const ctx = departmentChart.value.getContext('2d')
		const centerX = 150
		const centerY = 150
		const radius = 100

		let currentAngle = 0

		departmentData.value.forEach((dept) => {
			const sliceAngle = (dept.value / 100) * 2 * Math.PI

			ctx.beginPath()
			ctx.moveTo(centerX, centerY)
			ctx.arc(centerX, centerY, radius, currentAngle, currentAngle + sliceAngle)
			ctx.closePath()
			ctx.fillStyle = dept.color
			ctx.fill()

			currentAngle += sliceAngle
		})
	}
}

// Lifecycle
onMounted(async () => {
	await nextTick()
	initCharts()
})
</script>

<style scoped>
canvas {
	max-width: 100%;
	height: auto;
}
</style>
