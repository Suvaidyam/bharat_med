<template>
	<div class="min-h-screen bg-gray-50 p-4 md:p-6">
		<!-- Header -->
		<div class="mb-8">
			<div class="flex flex-col md:flex-row md:items-center md:justify-between gap-4">
				<div>
					<h1 class="text-2xl md:text-3xl font-bold text-gray-900">Inventory Report</h1>
					<p class="text-gray-600 mt-1">
						Track inventory levels, usage patterns, and supply chain metrics
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
						v-model="selectedCategory"
						class="bg-white px-3 py-2 rounded-lg border text-sm"
					>
						<option value="all">All Categories</option>
						<option value="medications">Medications</option>
						<option value="medical-supplies">Medical Supplies</option>
						<option value="equipment">Equipment</option>
						<option value="office-supplies">Office Supplies</option>
						<option value="laboratory">Laboratory</option>
					</select>

					<select
						v-model="selectedSupplier"
						class="bg-white px-3 py-2 rounded-lg border text-sm"
					>
						<option value="all">All Suppliers</option>
						<option value="medline">Medline Industries</option>
						<option value="mckesson">McKesson</option>
						<option value="cardinal">Cardinal Health</option>
						<option value="pharma-tech">Pharma Tech</option>
					</select>

					<div class="relative">
						<input
							type="text"
							placeholder="Search inventory items..."
							v-model="searchQuery"
							class="pl-10 pr-4 py-2 border border-gray-300 rounded-lg text-sm focus:ring-2 focus:ring-blue-500 focus:border-blue-500 w-64"
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
			<!-- Total Items -->
			<div class="bg-white p-6 rounded-xl shadow-sm border">
				<div class="flex items-center justify-between mb-4">
					<h3 class="text-sm font-medium text-gray-600">Total Items</h3>
					<div class="p-2 bg-gray-100 rounded-lg">
						<svg
							class="w-5 h-5 text-gray-600"
							fill="none"
							stroke="currentColor"
							viewBox="0 0 24 24"
						>
							<path
								stroke-linecap="round"
								stroke-linejoin="round"
								stroke-width="2"
								d="M20 7l-8-4-8 4m16 0l-8 4-8-4m16 0v10l-8 4-8-4V7"
							/>
						</svg>
					</div>
				</div>
				<div class="text-3xl font-bold text-gray-900 mb-2">1,245</div>
				<div class="flex items-center text-sm text-gray-500">
					<span class="text-green-600">+5.2%</span>
					<span class="ml-1">from since last month</span>
				</div>
			</div>

			<!-- Low Stock Items -->
			<div class="bg-white p-6 rounded-xl shadow-sm border">
				<div class="flex items-center justify-between mb-4">
					<h3 class="text-sm font-medium text-gray-600">Low Stock Items</h3>
					<div class="p-2 bg-red-100 rounded-lg">
						<div
							class="w-5 h-5 bg-red-500 rounded-full flex items-center justify-center"
						>
							<span class="text-white text-xs font-bold">32</span>
						</div>
					</div>
				</div>
				<div class="text-3xl font-bold text-gray-900 mb-2">2.6%</div>
				<div class="flex items-center text-sm text-gray-500">
					<span class="text-red-600">-0.8%</span>
					<span class="ml-1">from previous period</span>
				</div>
			</div>

			<!-- Expiring Soon -->
			<div class="bg-white p-6 rounded-xl shadow-sm border">
				<div class="flex items-center justify-between mb-4">
					<h3 class="text-sm font-medium text-gray-600">Expiring Soon</h3>
					<div class="p-2 bg-yellow-100 rounded-lg">
						<div
							class="w-5 h-5 bg-yellow-500 rounded-full flex items-center justify-center"
						>
							<span class="text-white text-xs font-bold">15</span>
						</div>
					</div>
				</div>
				<div class="text-3xl font-bold text-gray-900 mb-2">1.4%</div>
				<div class="flex items-center text-sm text-gray-500">
					<span class="text-green-600">0.3%</span>
					<span class="ml-1">from previous period</span>
				</div>
			</div>

			<!-- Inventory Value -->
			<div class="bg-white p-6 rounded-xl shadow-sm border">
				<div class="flex items-center justify-between mb-4">
					<h3 class="text-sm font-medium text-gray-600">Inventory Value</h3>
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
				<div class="text-3xl font-bold text-gray-900 mb-2">$248,320</div>
				<div class="flex items-center text-sm text-gray-500">
					<span class="text-green-600">+4.2%</span>
					<span class="ml-1">from previous period</span>
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
			<!-- Inventory by Category Chart -->
			<div class="bg-white p-6 rounded-xl shadow-sm border">
				<h3 class="text-lg font-semibold text-gray-900 mb-2">Inventory by Category</h3>
				<p class="text-sm text-gray-600 mb-6">
					Distribution of inventory items by category
				</p>

				<!-- Pie Chart Container -->
				<div class="h-80 flex items-center justify-center">
					<canvas
						ref="categoryChart"
						width="300"
						height="300"
						class="max-w-full"
					></canvas>
				</div>

				<!-- Legend -->
				<div class="flex flex-wrap justify-center gap-4 mt-4">
					<div
						v-for="category in categoryData"
						:key="category.name"
						class="flex items-center gap-2"
					>
						<div
							class="w-3 h-3 rounded-full"
							:style="{ backgroundColor: category.color }"
						></div>
						<span class="text-sm text-gray-600">{{ category.name }}</span>
					</div>
				</div>
			</div>

			<!-- Stock Status Distribution -->
			<div class="bg-white p-6 rounded-xl shadow-sm border">
				<h3 class="text-lg font-semibold text-gray-900 mb-2">Stock Status Distribution</h3>
				<p class="text-sm text-gray-600 mb-6">Current stock status of inventory items</p>

				<!-- Donut Chart Container -->
				<div class="h-80 flex items-center justify-center">
					<canvas ref="statusChart" width="300" height="300" class="max-w-full"></canvas>
				</div>

				<!-- Legend -->
				<div class="flex flex-wrap justify-center gap-4 mt-4">
					<div
						v-for="status in statusData"
						:key="status.name"
						class="flex items-center gap-2"
					>
						<div
							class="w-3 h-3 rounded-full"
							:style="{ backgroundColor: status.color }"
						></div>
						<span class="text-sm text-gray-600">{{ status.name }}</span>
					</div>
				</div>
			</div>
		</div>

		<!-- Low Stock Items Table -->
		<div class="bg-white rounded-xl shadow-sm border">
			<div class="p-6 border-b border-gray-200">
				<div class="flex flex-col md:flex-row md:items-center md:justify-between gap-4">
					<div>
						<h3 class="text-lg font-semibold text-gray-900">Top Low Stock Items</h3>
						<p class="text-sm text-gray-600">Items that need immediate attention</p>
					</div>

					<button
						class="flex items-center gap-2 px-3 py-2 border border-gray-300 rounded-lg text-sm hover:bg-gray-50"
					>
						<svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
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

			<!-- Table -->
			<div class="overflow-x-auto">
				<table class="w-full">
					<thead class="bg-gray-50">
						<tr>
							<th
								class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
							>
								Item Name
							</th>
							<th
								class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
							>
								Category
							</th>
							<th
								class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
							>
								Current Stock
							</th>
							<th
								class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
							>
								Reorder Level
							</th>
							<th
								class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
							>
								Supplier
							</th>
							<th
								class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
							>
								Status
							</th>
						</tr>
					</thead>
					<tbody class="bg-white divide-y divide-gray-200">
						<tr
							v-for="item in filteredInventoryData"
							:key="item.id"
							class="hover:bg-gray-50"
						>
							<td class="px-6 py-4 whitespace-nowrap">
								<div class="text-sm font-medium text-gray-900">
									{{ item.name }}
								</div>
							</td>
							<td class="px-6 py-4 whitespace-nowrap text-sm text-gray-900">
								{{ item.category }}
							</td>
							<td class="px-6 py-4 whitespace-nowrap text-sm text-gray-900">
								{{ item.currentStock }}
							</td>
							<td class="px-6 py-4 whitespace-nowrap text-sm text-gray-900">
								{{ item.reorderLevel }}
							</td>
							<td class="px-6 py-4 whitespace-nowrap text-sm text-gray-900">
								{{ item.supplier }}
							</td>
							<td class="px-6 py-4 whitespace-nowrap">
								<span
									:class="getStatusClass(item.status)"
									class="inline-flex px-2 py-1 text-xs font-semibold rounded-full"
								>
									{{ item.status }}
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
const selectedCategory = ref('all')
const selectedSupplier = ref('all')
const activeTab = ref('overview')
const searchQuery = ref('')

// Chart refs
const categoryChart = ref(null)
const statusChart = ref(null)

// Navigation tabs
const tabs = ref([
	{ id: 'overview', name: 'Overview' },
	{ id: 'stock-levels', name: 'Stock Levels' },
	{ id: 'usage-trends', name: 'Usage Trends' },
	{ id: 'suppliers', name: 'Suppliers' },
])

// Category data for pie chart
const categoryData = ref([
	{ name: 'Medications', value: 35, color: '#8B5CF6' },
	{ name: 'Medical Supplies', value: 28, color: '#10B981' },
	{ name: 'Equipment', value: 18, color: '#F59E0B' },
	{ name: 'Office Supplies', value: 12, color: '#EF4444' },
	{ name: 'Laboratory', value: 7, color: '#3B82F6' },
])

// Status data for donut chart
const statusData = ref([
	{ name: 'In Stock', value: 85, color: '#10B981' },
	{ name: 'Low Stock', value: 12, color: '#F59E0B' },
	{ name: 'Out of Stock', value: 3, color: '#EF4444' },
])

// Inventory data
const inventoryData = ref([
	{
		id: 1,
		name: 'Surgical Gloves (M)',
		category: 'Medical Supplies',
		currentStock: '24 boxes',
		reorderLevel: '50 boxes',
		supplier: 'Medline Industries',
		status: 'Critical',
	},
	{
		id: 2,
		name: 'Ibuprofen 200mg',
		category: 'Medications',
		currentStock: '15 bottles',
		reorderLevel: '30 bottles',
		supplier: 'McKesson',
		status: 'Critical',
	},
	{
		id: 3,
		name: 'Gauze Pads 4x4',
		category: 'Medical Supplies',
		currentStock: '32 packs',
		reorderLevel: '60 packs',
		supplier: 'Cardinal Health',
		status: 'Low',
	},
	{
		id: 4,
		name: 'Blood Pressure Cuffs',
		category: 'Equipment',
		currentStock: '8 units',
		reorderLevel: '15 units',
		supplier: 'Medline Industries',
		status: 'Low',
	},
	{
		id: 5,
		name: 'Thermometers Digital',
		category: 'Equipment',
		currentStock: '12 units',
		reorderLevel: '20 units',
		supplier: 'Pharma Tech',
		status: 'Low',
	},
])

// Computed properties
const filteredInventoryData = computed(() => {
	let filtered = inventoryData.value

	if (searchQuery.value) {
		filtered = filtered.filter(
			(item) =>
				item.name.toLowerCase().includes(searchQuery.value.toLowerCase()) ||
				item.category.toLowerCase().includes(searchQuery.value.toLowerCase()) ||
				item.supplier.toLowerCase().includes(searchQuery.value.toLowerCase()),
		)
	}

	if (selectedCategory.value !== 'all') {
		filtered = filtered.filter(
			(item) => item.category.toLowerCase().replace(' ', '-') === selectedCategory.value,
		)
	}

	if (selectedSupplier.value !== 'all') {
		filtered = filtered.filter(
			(item) => item.supplier.toLowerCase().replace(' ', '-') === selectedSupplier.value,
		)
	}

	return filtered
})

// Helper functions
const getStatusClass = (status) => {
	switch (status.toLowerCase()) {
		case 'critical':
			return 'bg-red-100 text-red-800'
		case 'low':
			return 'bg-yellow-100 text-yellow-800'
		case 'normal':
			return 'bg-green-100 text-green-800'
		default:
			return 'bg-gray-100 text-gray-800'
	}
}

// Chart functions
const drawPieChart = (canvas, data, title) => {
	const ctx = canvas.getContext('2d')
	const centerX = canvas.width / 2
	const centerY = canvas.height / 2
	const radius = Math.min(centerX, centerY) - 20

	let currentAngle = 0
	const total = data.reduce((sum, item) => sum + item.value, 0)

	// Clear canvas
	ctx.clearRect(0, 0, canvas.width, canvas.height)

	data.forEach((item) => {
		const sliceAngle = (item.value / total) * 2 * Math.PI

		// Draw slice
		ctx.beginPath()
		ctx.moveTo(centerX, centerY)
		ctx.arc(centerX, centerY, radius, currentAngle, currentAngle + sliceAngle)
		ctx.closePath()
		ctx.fillStyle = item.color
		ctx.fill()

		// Draw border
		ctx.strokeStyle = '#ffffff'
		ctx.lineWidth = 2
		ctx.stroke()

		currentAngle += sliceAngle
	})
}

const drawDonutChart = (canvas, data) => {
	const ctx = canvas.getContext('2d')
	const centerX = canvas.width / 2
	const centerY = canvas.height / 2
	const outerRadius = Math.min(centerX, centerY) - 20
	const innerRadius = outerRadius * 0.6

	let currentAngle = 0
	const total = data.reduce((sum, item) => sum + item.value, 0)

	// Clear canvas
	ctx.clearRect(0, 0, canvas.width, canvas.height)

	data.forEach((item) => {
		const sliceAngle = (item.value / total) * 2 * Math.PI

		// Draw outer arc
		ctx.beginPath()
		ctx.arc(centerX, centerY, outerRadius, currentAngle, currentAngle + sliceAngle)
		ctx.arc(centerX, centerY, innerRadius, currentAngle + sliceAngle, currentAngle, true)
		ctx.closePath()
		ctx.fillStyle = item.color
		ctx.fill()

		// Draw border
		ctx.strokeStyle = '#ffffff'
		ctx.lineWidth = 2
		ctx.stroke()

		currentAngle += sliceAngle
	})
}

// Initialize charts
const initCharts = () => {
	if (categoryChart.value) {
		drawPieChart(categoryChart.value, categoryData.value, 'Inventory by Category')
	}

	if (statusChart.value) {
		drawDonutChart(statusChart.value, statusData.value)
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
