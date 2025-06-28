<template>
	<div class="min-h-screen p-4 md:p-6">
		<!-- Header -->
		<div class="mb-6">
			<div class="flex items-center mb-4">
				<button class="mr-4 p-2 hover:bg-gray-100 rounded-lg">
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
							d="M15 19l-7-7 7-7"
						></path>
					</svg>
				</button>
				<div>
					<h1 class="text-2xl font-semibold text-gray-900">Payments History</h1>
					<p class="text-sm text-gray-500">View and manage all payment transactions.</p>
				</div>
			</div>

			<!-- Search and Filters -->
			<div
				class="flex flex-col sm:flex-row gap-4 items-start sm:items-center justify-between"
			>
				<div class="flex flex-col sm:flex-row gap-4 flex-1">
					<div class="relative">
						<svg
							class="absolute left-3 top-1/2 transform -translate-y-1/2 w-4 h-4 text-gray-400"
							fill="none"
							stroke="currentColor"
							viewBox="0 0 24 24"
						>
							<path
								stroke-linecap="round"
								stroke-linejoin="round"
								stroke-width="2"
								d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"
							></path>
						</svg>
						<input
							v-model="searchQuery"
							type="text"
							placeholder="Search payments..."
							class="pl-10 pr-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent w-full sm:w-64"
						/>
					</div>
					<select
						v-model="selectedMethod"
						class="px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
					>
						<option value="">All Methods</option>
						<option value="Credit Card">Credit Card</option>
						<option value="Debit Card">Debit Card</option>
						<option value="Check">Check</option>
						<option value="Cash">Cash</option>
						<option value="Bank Transfer">Bank Transfer</option>
						<option value="Insurance">Insurance</option>
					</select>
					<button
						class="px-4 py-2 bg-gray-100 text-gray-700 rounded-lg hover:bg-gray-200 flex items-center"
					>
						<svg
							class="w-4 h-4 mr-2"
							fill="none"
							stroke="currentColor"
							viewBox="0 0 24 24"
						>
							<path
								stroke-linecap="round"
								stroke-linejoin="round"
								stroke-width="2"
								d="M12 10v6m0 0l-3-3m3 3l3-3m2 8H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"
							></path>
						</svg>
						Export
					</button>
				</div>
				<div class="text-sm text-gray-500">Jan 26, 2025 - Jun 28, 2025</div>
			</div>
		</div>

		<!-- Tabs -->
		<div class="mb-6">
			<div class="flex space-x-1 bg-gray-100 rounded-lg p-1 w-fit">
				<button
					v-for="tab in tabs"
					:key="tab.id"
					@click="activeTab = tab.id"
					:class="[
						'px-4 py-2 rounded-md text-sm font-medium transition-colors',
						activeTab === tab.id
							? 'bg-white text-gray-900 shadow-sm'
							: 'text-gray-600 hover:text-gray-900',
					]"
				>
					{{ tab.label }}
				</button>
			</div>
		</div>

		<!-- Main Content -->
		<div class="bg-white rounded-lg shadow">
			<!-- Table Header -->
			<div class="px-6 py-4 border-b border-gray-200">
				<div class="flex items-center justify-between">
					<h2 class="text-lg font-medium text-gray-900">All Payments</h2>
					<select
						v-model="sortOrder"
						class="text-sm border border-gray-300 rounded px-3 py-1"
					>
						<option value="newest">Newest First</option>
						<option value="oldest">Oldest First</option>
						<option value="amount-high">Amount: High to Low</option>
						<option value="amount-low">Amount: Low to High</option>
					</select>
				</div>
				<p class="text-sm text-gray-500 mt-1">View all payment transactions.</p>
			</div>

			<!-- Desktop Table -->
			<div class="hidden lg:block overflow-x-auto">
				<table class="w-full">
					<thead class="bg-gray-50">
						<tr>
							<th
								class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
							>
								Payment ID
							</th>
							<th
								class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
							>
								Patient
							</th>
							<th
								class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
							>
								Invoice
							</th>
							<th
								class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
							>
								Date
							</th>
							<th
								class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
							>
								Amount
							</th>
							<th
								class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
							>
								Method
							</th>
							<th
								class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
							>
								Status
							</th>
							<th
								class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
							>
								Actions
							</th>
						</tr>
					</thead>
					<tbody class="bg-white divide-y divide-gray-200">
						<tr
							v-for="payment in filteredPayments"
							:key="payment.id"
							class="hover:bg-gray-50"
						>
							<td
								class="px-6 py-4 whitespace-nowrap text-sm font-medium text-gray-900"
							>
								{{ payment.id }}
							</td>
							<td class="px-6 py-4 whitespace-nowrap">
								<div class="flex items-center">
									<div class="flex-shrink-0 h-8 w-8">
										<div
											class="h-8 w-8 rounded-full bg-gradient-to-r from-blue-400 to-purple-500 flex items-center justify-center"
										>
											<span class="text-white text-sm font-medium">{{
												getInitials(payment.patient.name)
											}}</span>
										</div>
									</div>
									<div class="ml-3">
										<div class="text-sm font-medium text-gray-900">
											{{ payment.patient.name }}
										</div>
										<div class="text-sm text-gray-500">
											{{ payment.patient.id }}
										</div>
									</div>
								</div>
							</td>
							<td class="px-6 py-4 whitespace-nowrap text-sm text-gray-900">
								{{ payment.invoice }}
							</td>
							<td class="px-6 py-4 whitespace-nowrap text-sm text-gray-900">
								{{ payment.date }}
							</td>
							<td
								class="px-6 py-4 whitespace-nowrap text-sm font-medium text-gray-900"
							>
								${{ payment.amount.toFixed(2) }}
							</td>
							<td class="px-6 py-4 whitespace-nowrap text-sm text-gray-900">
								{{ payment.method }}
							</td>
							<td class="px-6 py-4 whitespace-nowrap">
								<span
									:class="getStatusClass(payment.status)"
									class="inline-flex px-2 py-1 text-xs font-medium rounded-full"
								>
									{{ payment.status }}
								</span>
							</td>
							<td class="px-6 py-4 whitespace-nowrap text-sm text-gray-400">
								<button class="hover:text-gray-600">
									<svg class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20">
										<path
											d="M10 6a2 2 0 110-4 2 2 0 010 4zM10 12a2 2 0 110-4 2 2 0 010 4zM10 18a2 2 0 110-4 2 2 0 010 4z"
										></path>
									</svg>
								</button>
							</td>
						</tr>
					</tbody>
				</table>
			</div>

			<!-- Mobile Cards -->
			<div class="lg:hidden">
				<div
					v-for="payment in filteredPayments"
					:key="payment.id"
					class="border-b border-gray-200 p-4"
				>
					<div class="flex items-center justify-between mb-3">
						<div class="flex items-center">
							<div
								class="h-10 w-10 rounded-full bg-gradient-to-r from-blue-400 to-purple-500 flex items-center justify-center mr-3"
							>
								<span class="text-white text-sm font-medium">{{
									getInitials(payment.patient.name)
								}}</span>
							</div>
							<div>
								<div class="font-medium text-gray-900">
									{{ payment.patient.name }}
								</div>
								<div class="text-sm text-gray-500">{{ payment.patient.id }}</div>
							</div>
						</div>
						<span
							:class="getStatusClass(payment.status)"
							class="inline-flex px-2 py-1 text-xs font-medium rounded-full"
						>
							{{ payment.status }}
						</span>
					</div>
					<div class="grid grid-cols-2 gap-3 text-sm">
						<div>
							<span class="text-gray-500">Payment ID:</span>
							<div class="font-medium">{{ payment.id }}</div>
						</div>
						<div>
							<span class="text-gray-500">Invoice:</span>
							<div class="font-medium">{{ payment.invoice }}</div>
						</div>
						<div>
							<span class="text-gray-500">Date:</span>
							<div class="font-medium">{{ payment.date }}</div>
						</div>
						<div>
							<span class="text-gray-500">Amount:</span>
							<div class="font-medium">${{ payment.amount.toFixed(2) }}</div>
						</div>
						<div>
							<span class="text-gray-500">Method:</span>
							<div class="font-medium">{{ payment.method }}</div>
						</div>
					</div>
				</div>
			</div>
		</div>

		<!-- Statistics Cards -->
		<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mt-8">
			<div class="bg-white rounded-lg shadow p-6">
				<h3 class="text-lg font-medium text-gray-900 mb-2">Total Payments</h3>
				<div class="text-3xl font-bold text-gray-900">${{ stats.total.toFixed(2) }}</div>
				<div class="text-sm text-gray-500">From {{ stats.totalCount }} transactions</div>
				<div class="w-full bg-gray-200 rounded-full h-2 mt-3">
					<div class="bg-green-500 h-2 rounded-full" style="width: 100%"></div>
				</div>
			</div>

			<div class="bg-white rounded-lg shadow p-6">
				<h3 class="text-lg font-medium text-gray-900 mb-2">Pending Payments</h3>
				<div class="text-3xl font-bold text-orange-600">
					${{ stats.pending.toFixed(2) }}
				</div>
				<div class="text-sm text-gray-500">From {{ stats.pendingCount }} transactions</div>
				<div class="w-full bg-gray-200 rounded-full h-2 mt-3">
					<div
						class="bg-orange-500 h-2 rounded-full"
						:style="`width: ${(stats.pending / stats.total) * 100}%`"
					></div>
				</div>
			</div>

			<div class="bg-white rounded-lg shadow p-6">
				<h3 class="text-lg font-medium text-gray-900 mb-2">Failed Payments</h3>
				<div class="text-3xl font-bold text-red-600">${{ stats.failed.toFixed(2) }}</div>
				<div class="text-sm text-gray-500">From {{ stats.failedCount }} transactions</div>
				<div class="w-full bg-gray-200 rounded-full h-2 mt-3">
					<div
						class="bg-red-500 h-2 rounded-full"
						:style="`width: ${(stats.failed / stats.total) * 100}%`"
					></div>
				</div>
			</div>

			<div class="bg-white rounded-lg shadow p-6">
				<h3 class="text-lg font-medium text-gray-900 mb-2">Payment Methods</h3>
				<div class="space-y-2">
					<div
						v-for="method in paymentMethodStats"
						:key="method.name"
						class="flex justify-between text-sm"
					>
						<span class="text-gray-600">{{ method.name }}</span>
						<span class="font-medium">{{ method.count }}</span>
					</div>
				</div>
			</div>
		</div>
	</div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'

// Reactive data
const searchQuery = ref('')
const selectedMethod = ref('')
const activeTab = ref('all')
const sortOrder = ref('newest')

const tabs = [
	{ id: 'all', label: 'All Payments' },
	{ id: 'completed', label: 'Completed' },
	{ id: 'pending', label: 'Pending' },
	{ id: 'failed', label: 'Failed' },
]

const payments = ref([
	{
		id: 'PMT-007',
		patient: { name: 'Michael Johnson', id: '506789' },
		invoice: 'INV-005',
		date: '2024-04-28',
		amount: 450.0,
		method: 'Check',
		status: 'Pending',
	},
	{
		id: 'PMT-006',
		patient: { name: 'Emily Davis', id: '723456' },
		invoice: 'INV-002',
		date: '2024-04-25',
		amount: 350.0,
		method: 'Credit Card',
		status: 'Failed',
	},
	{
		id: 'PMT-001',
		patient: { name: 'John Smith', id: '678945' },
		invoice: 'INV-001',
		date: '2024-04-22',
		amount: 200.0,
		method: 'Credit Card',
		status: 'Completed',
	},
	{
		id: 'PMT-002',
		patient: { name: 'Robert Wilson', id: '456789' },
		invoice: 'INV-003',
		date: '2024-04-20',
		amount: 175.0,
		method: 'Debit Card',
		status: 'Completed',
	},
	{
		id: 'PMT-003',
		patient: { name: 'Jessica Brown', id: '389745' },
		invoice: 'INV-004',
		date: '2024-04-18',
		amount: 520.0,
		method: 'Bank Transfer',
		status: 'Completed',
	},
	{
		id: 'PMT-004',
		patient: { name: 'Sarah Thompson', id: '234567' },
		invoice: 'INV-006',
		date: '2024-04-15',
		amount: 300.0,
		method: 'Cash',
		status: 'Completed',
	},
	{
		id: 'PMT-005',
		patient: { name: 'John Smith', id: '678945' },
		invoice: 'INV-001',
		date: '2024-04-10',
		amount: 50.0,
		method: 'Insurance',
		status: 'Processing',
	},
])

// Computed properties
const filteredPayments = computed(() => {
	let filtered = payments.value

	// Filter by tab
	if (activeTab.value !== 'all') {
		filtered = filtered.filter((payment) => {
			if (activeTab.value === 'completed') return payment.status === 'Completed'
			if (activeTab.value === 'pending')
				return payment.status === 'Pending' || payment.status === 'Processing'
			if (activeTab.value === 'failed') return payment.status === 'Failed'
			return true
		})
	}

	// Filter by search query
	if (searchQuery.value) {
		const query = searchQuery.value.toLowerCase()
		filtered = filtered.filter(
			(payment) =>
				payment.patient.name.toLowerCase().includes(query) ||
				payment.id.toLowerCase().includes(query) ||
				payment.invoice.toLowerCase().includes(query),
		)
	}

	// Filter by payment method
	if (selectedMethod.value) {
		filtered = filtered.filter((payment) => payment.method === selectedMethod.value)
	}

	// Sort
	filtered.sort((a, b) => {
		switch (sortOrder.value) {
			case 'newest':
				return new Date(b.date) - new Date(a.date)
			case 'oldest':
				return new Date(a.date) - new Date(b.date)
			case 'amount-high':
				return b.amount - a.amount
			case 'amount-low':
				return a.amount - b.amount
			default:
				return 0
		}
	})

	return filtered
})

const stats = computed(() => {
	const total = payments.value.reduce((sum, payment) => sum + payment.amount, 0)
	const pending = payments.value
		.filter((p) => p.status === 'Pending' || p.status === 'Processing')
		.reduce((sum, payment) => sum + payment.amount, 0)
	const failed = payments.value
		.filter((p) => p.status === 'Failed')
		.reduce((sum, payment) => sum + payment.amount, 0)

	return {
		total,
		pending,
		failed,
		totalCount: payments.value.length,
		pendingCount: payments.value.filter(
			(p) => p.status === 'Pending' || p.status === 'Processing',
		).length,
		failedCount: payments.value.filter((p) => p.status === 'Failed').length,
	}
})

const paymentMethodStats = computed(() => {
	const methods = {}
	payments.value.forEach((payment) => {
		methods[payment.method] = (methods[payment.method] || 0) + 1
	})

	return Object.entries(methods)
		.map(([name, count]) => ({ name, count }))
		.sort((a, b) => b.count - a.count)
})

// Methods
const getInitials = (name) => {
	return name
		.split(' ')
		.map((n) => n[0])
		.join('')
		.toUpperCase()
}

const getStatusClass = (status) => {
	switch (status) {
		case 'Completed':
			return 'bg-green-100 text-green-800'
		case 'Pending':
			return 'bg-yellow-100 text-yellow-800'
		case 'Processing':
			return 'bg-blue-100 text-blue-800'
		case 'Failed':
			return 'bg-red-100 text-red-800'
		default:
			return 'bg-gray-100 text-gray-800'
	}
}
</script>
