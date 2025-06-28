<template>
	<div class="min-h-screen">
		<!-- Header -->
		<div class="bg-white shadow-sm border-b border-gray-200">
			<div class="px-4 sm:px-6 lg:px-8">
				<div class="flex justify-between items-center py-4">
					<div>
						<h1 class="text-2xl font-semibold text-gray-900">Invoices</h1>
						<p class="text-sm text-gray-600">
							Manage billing and invoices for your patients.
						</p>
					</div>
					<div class="flex space-x-3">
						<button
							class="px-4 py-2 text-sm font-medium text-gray-700 bg-white border border-gray-300 rounded-md hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500"
						>
							Payments
						</button>
						<button
							class="px-4 py-2 text-sm font-medium text-gray-700 bg-white border border-gray-300 rounded-md hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500"
						>
							Insurance Claims
						</button>
						<button
							class="px-4 py-2 text-sm font-medium text-white bg-gray-900 border border-transparent rounded-md hover:bg-gray-800 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-gray-500"
						>
							+ Create Invoice
						</button>
					</div>
				</div>
			</div>
		</div>

		<div class="px-4 sm:px-6 lg:px-8 py-6">
			<!-- Tabs -->
			<div class="border-b border-gray-200 mb-6">
				<nav class="-mb-px flex space-x-8">
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

			<!-- Search and Filter -->
			<div class="flex flex-col sm:flex-row sm:items-center sm:justify-between mb-6">
				<div class="mb-4 sm:mb-0">
					<h2 class="text-lg font-medium text-gray-900">All Invoices</h2>
					<p class="text-sm text-gray-600">
						Showing all {{ invoices.length }} invoices.
					</p>
				</div>
				<div class="flex items-center space-x-3">
					<div class="relative">
						<input
							v-model="searchQuery"
							type="text"
							placeholder="Search invoices..."
							class="pl-10 pr-4 py-2 border border-gray-300 rounded-md focus:ring-blue-500 focus:border-blue-500 text-sm"
						/>
						<div
							class="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none"
						>
							<svg
								class="h-5 w-5 text-gray-400"
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
					</div>
					<button class="p-2 border border-gray-300 rounded-md hover:bg-gray-50">
						<svg
							class="h-5 w-5 text-gray-400"
							fill="none"
							stroke="currentColor"
							viewBox="0 0 24 24"
						>
							<path
								stroke-linecap="round"
								stroke-linejoin="round"
								stroke-width="2"
								d="M3 4a1 1 0 011-1h16a1 1 0 011 1v2.586a1 1 0 01-.293.707l-6.414 6.414a1 1 0 00-.293.707V17l-4 4v-6.586a1 1 0 00-.293-.707L3.293 7.707A1 1 0 013 7V4z"
							/>
						</svg>
					</button>
					<select
						class="text-sm border border-gray-300 rounded-md px-3 py-2 bg-white focus:ring-blue-500 focus:border-blue-500"
					>
						<option>Newest First</option>
						<option>Oldest First</option>
						<option>Amount: High to Low</option>
						<option>Amount: Low to High</option>
					</select>
				</div>
			</div>

			<!-- Invoice Table -->
			<div class="bg-white shadow overflow-hidden sm:rounded-md">
				<div class="overflow-x-auto">
					<table class="min-w-full divide-y divide-gray-200">
						<thead class="bg-gray-50">
							<tr>
								<th
									class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
								>
									Invoice #
								</th>
								<th
									class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
								>
									Patient
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
									Balance
								</th>
								<th
									class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
								>
									Status
								</th>
								<th
									class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
								>
									Insurance
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
								v-for="invoice in filteredInvoices"
								:key="invoice.id"
								class="hover:bg-gray-50"
							>
								<td
									class="px-6 py-4 whitespace-nowrap text-sm font-medium text-gray-900"
								>
									{{ invoice.invoiceNumber }}
								</td>
								<td class="px-6 py-4 whitespace-nowrap">
									<div class="flex items-center">
										<div
											class="h-8 w-8 rounded-full bg-gradient-to-r from-blue-500 to-purple-600 flex items-center justify-center text-white text-sm font-medium"
										>
											{{ invoice.patient.initials }}
										</div>
										<div class="ml-3">
											<div class="text-sm font-medium text-gray-900">
												{{ invoice.patient.name }}
											</div>
											<div class="text-sm text-gray-500">
												{{ invoice.patient.id }}
											</div>
										</div>
									</div>
								</td>
								<td class="px-6 py-4 whitespace-nowrap">
									<div class="text-sm text-gray-900">{{ invoice.date }}</div>
									<div class="text-sm text-gray-500">
										Due: {{ invoice.dueDate }}
									</div>
								</td>
								<td class="px-6 py-4 whitespace-nowrap text-sm text-gray-900">
									${{ invoice.amount.toFixed(2) }}
								</td>
								<td class="px-6 py-4 whitespace-nowrap text-sm text-gray-900">
									${{ invoice.balance.toFixed(2) }}
								</td>
								<td class="px-6 py-4 whitespace-nowrap">
									<span
										:class="getStatusBadgeClass(invoice.status)"
										class="inline-flex px-2 py-1 text-xs font-semibold rounded-full"
									>
										{{ invoice.status }}
									</span>
								</td>
								<td class="px-6 py-4 whitespace-nowrap">
									<span
										:class="getInsuranceBadgeClass(invoice.insurance)"
										class="inline-flex px-2 py-1 text-xs font-semibold rounded-full"
									>
										{{ invoice.insurance }}
									</span>
								</td>
								<td
									class="px-6 py-4 whitespace-nowrap text-right text-sm font-medium"
								>
									<button class="text-gray-400 hover:text-gray-600">
										<svg
											class="h-5 w-5"
											fill="currentColor"
											viewBox="0 0 20 20"
										>
											<path
												d="M10 6a2 2 0 110-4 2 2 0 010 4zM10 12a2 2 0 110-4 2 2 0 010 4zM10 18a2 2 0 110-4 2 2 0 010 4z"
											/>
										</svg>
									</button>
								</td>
							</tr>
						</tbody>
					</table>
				</div>
			</div>

			<!-- Summary Cards -->
			<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mt-8">
				<div class="bg-white overflow-hidden shadow rounded-lg">
					<div class="p-5">
						<div class="flex items-center">
							<div class="flex-shrink-0">
								<div
									class="w-8 h-8 bg-red-100 rounded-md flex items-center justify-center"
								>
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
											d="M12 8c-1.657 0-3 .895-3 2s1.343 2 3 2 3 .895 3 2-1.343 2-3 2m0-8c1.11 0 2.08.402 2.599 1M12 8V7m0 1v8m0 0v1m0-1c-1.11 0-2.08-.402-2.599-1"
										/>
									</svg>
								</div>
							</div>
							<div class="ml-5 w-0 flex-1">
								<dl>
									<dt class="text-sm font-medium text-gray-500 truncate">
										Total Outstanding
									</dt>
									<dd class="text-lg font-medium text-gray-900">$1030.00</dd>
								</dl>
							</div>
						</div>
					</div>
				</div>

				<div class="bg-white overflow-hidden shadow rounded-lg">
					<div class="p-5">
						<div class="flex items-center">
							<div class="flex-shrink-0">
								<div
									class="w-8 h-8 bg-green-100 rounded-md flex items-center justify-center"
								>
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
											d="M5 13l4 4L19 7"
										/>
									</svg>
								</div>
							</div>
							<div class="ml-5 w-0 flex-1">
								<dl>
									<dt class="text-sm font-medium text-gray-500 truncate">
										Paid This Month
									</dt>
									<dd class="text-lg font-medium text-gray-900">$1,245.00</dd>
									<dd class="text-sm text-green-600">+2% from last month</dd>
								</dl>
							</div>
						</div>
					</div>
				</div>

				<div class="bg-white overflow-hidden shadow rounded-lg">
					<div class="p-5">
						<div class="flex items-center">
							<div class="flex-shrink-0">
								<div
									class="w-8 h-8 bg-orange-100 rounded-md flex items-center justify-center"
								>
									<svg
										class="w-5 h-5 text-orange-600"
										fill="none"
										stroke="currentColor"
										viewBox="0 0 24 24"
									>
										<path
											stroke-linecap="round"
											stroke-linejoin="round"
											stroke-width="2"
											d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-2.5L13.732 4c-.77-.833-1.964-.833-2.732 0L3.732 16.5c-.77.833.192 2.5 1.732 2.5z"
										/>
									</svg>
								</div>
							</div>
							<div class="ml-5 w-0 flex-1">
								<dl>
									<dt class="text-sm font-medium text-gray-500 truncate">
										Overdue Invoices
									</dt>
									<dd class="text-lg font-medium text-gray-900">4</dd>
									<dd class="text-sm text-orange-600">Total: $980.00</dd>
								</dl>
							</div>
						</div>
					</div>
				</div>

				<div class="bg-white overflow-hidden shadow rounded-lg">
					<div class="p-5">
						<div class="flex items-center">
							<div class="flex-shrink-0">
								<div
									class="w-8 h-8 bg-blue-100 rounded-md flex items-center justify-center"
								>
									<svg
										class="w-5 h-5 text-blue-600"
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
							<div class="ml-5 w-0 flex-1">
								<dl>
									<dt class="text-sm font-medium text-gray-500 truncate">
										Insurance Claims
									</dt>
									<dd class="text-lg font-medium text-gray-900">5</dd>
									<dd class="text-sm text-blue-600">Total: $1,640.00</dd>
								</dl>
							</div>
						</div>
					</div>
				</div>
			</div>
		</div>
	</div>
</template>

<script setup>
import { ref, computed } from 'vue'

const activeTab = ref('all')
const searchQuery = ref('')

const tabs = [
	{ id: 'all', name: 'All Invoices' },
	{ id: 'unpaid', name: 'Unpaid' },
	{ id: 'paid', name: 'Paid' },
	{ id: 'partially-paid', name: 'Partially Paid' },
]

const invoices = ref([
	{
		id: 'INV-007',
		invoiceNumber: 'INV-007',
		patient: { name: 'David Miller', id: 'P7024', initials: 'DM' },
		date: '2024-04-20',
		dueDate: '2024-05-20',
		amount: 180.0,
		balance: 180.0,
		status: 'Unpaid',
		insurance: 'Not Submitted',
	},
	{
		id: 'INV-005',
		invoiceNumber: 'INV-005',
		patient: { name: 'Michael Johnson', id: 'P5013', initials: 'MJ' },
		date: '2024-04-18',
		dueDate: '2024-05-18',
		amount: 450.0,
		balance: 450.0,
		status: 'Unpaid',
		insurance: 'Submitted',
	},
	{
		id: 'INV-002',
		invoiceNumber: 'INV-002',
		patient: { name: 'Emily Davis', id: 'P2106', initials: 'ED' },
		date: '2024-04-16',
		dueDate: '2024-05-16',
		amount: 350.0,
		balance: 350.0,
		status: 'Unpaid',
		insurance: 'Pending',
	},
	{
		id: 'INV-001',
		invoiceNumber: 'INV-001',
		patient: { name: 'John Smith', id: 'P2343', initials: 'JS' },
		date: '2024-04-15',
		dueDate: '2024-05-15',
		amount: 250.0,
		balance: 50.0,
		status: 'Partially Paid',
		insurance: 'Approved',
	},
	{
		id: 'INV-006',
		invoiceNumber: 'INV-006',
		patient: { name: 'Sarah Thompson', id: 'P6098', initials: 'ST' },
		date: '2024-04-12',
		dueDate: '2024-05-12',
		amount: 300.0,
		balance: 0.0,
		status: 'Paid',
		insurance: 'Approved',
	},
	{
		id: 'INV-003',
		invoiceNumber: 'INV-003',
		patient: { name: 'Robert Wilson', id: 'P4507', initials: 'RW' },
		date: '2024-04-10',
		dueDate: '2024-05-10',
		amount: 175.0,
		balance: 0.0,
		status: 'Paid',
		insurance: 'Approved',
	},
	{
		id: 'INV-004',
		invoiceNumber: 'INV-004',
		patient: { name: 'Jessica Brown', id: 'P8551', initials: 'JB' },
		date: '2024-04-05',
		dueDate: '2024-05-05',
		amount: 520.0,
		balance: 0.0,
		status: 'Paid',
		insurance: 'Approved',
	},
])

const filteredInvoices = computed(() => {
	let filtered = invoices.value

	if (activeTab.value !== 'all') {
		filtered = filtered.filter((invoice) => {
			switch (activeTab.value) {
				case 'unpaid':
					return invoice.status === 'Unpaid'
				case 'paid':
					return invoice.status === 'Paid'
				case 'partially-paid':
					return invoice.status === 'Partially Paid'
				default:
					return true
			}
		})
	}

	if (searchQuery.value) {
		const query = searchQuery.value.toLowerCase()
		filtered = filtered.filter(
			(invoice) =>
				invoice.patient.name.toLowerCase().includes(query) ||
				invoice.invoiceNumber.toLowerCase().includes(query) ||
				invoice.patient.id.toLowerCase().includes(query),
		)
	}

	return filtered
})

const getStatusBadgeClass = (status) => {
	switch (status) {
		case 'Paid':
			return 'bg-green-100 text-green-800'
		case 'Unpaid':
			return 'bg-red-100 text-red-800'
		case 'Partially Paid':
			return 'bg-yellow-100 text-yellow-800'
		default:
			return 'bg-gray-100 text-gray-800'
	}
}

const getInsuranceBadgeClass = (insurance) => {
	switch (insurance) {
		case 'Approved':
			return 'bg-green-100 text-green-800'
		case 'Submitted':
			return 'bg-blue-100 text-blue-800'
		case 'Pending':
			return 'bg-yellow-100 text-yellow-800'
		case 'Not Submitted':
			return 'bg-gray-100 text-gray-800'
		default:
			return 'bg-gray-100 text-gray-800'
	}
}
</script>
