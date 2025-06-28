<template>
	<div class="p-6">
		<!-- Header -->
		<div class="flex justify-between items-center mb-4">
			<h1 class="text-2xl font-semibold">Stock Alerts</h1>
			<div class="flex items-center gap-2">
				<button
					class="flex items-center gap-1 text-sm px-3 py-2 bg-gray-100 rounded hover:bg-gray-200"
				>
					<span class="material-icons text-sm">download</span> Export
				</button>
				<button class="p-2 bg-gray-100 rounded hover:bg-gray-200">
					<span class="material-icons text-sm">settings</span>
				</button>
			</div>
		</div>
		<p class="text-sm text-gray-500 mb-6">Monitor and manage inventory alerts</p>

		<!-- Alert Cards -->
		<div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-4 gap-4 mb-6">
			<AlertCard
				title="Low Stock Items"
				count="7"
				subtitle="+8 since last week"
				icon="info"
			/>
			<AlertCard
				title="Out of Stock Items"
				count="5"
				subtitle="+3 since last week"
				icon="error"
			/>
			<AlertCard
				title="Expiring Soon"
				count="6"
				subtitle="Within next 30 days"
				icon="event"
			/>
			<AlertCard
				title="Pending Orders"
				count="7"
				subtitle="View orders"
				icon="shopping_cart"
			/>
		</div>

		<!-- Filters -->
		<div class="flex flex-wrap gap-4 items-center mb-4">
			<input
				type="text"
				placeholder="Search alerts..."
				class="border border-gray-300 px-3 py-2 rounded w-full sm:w-60"
			/>
			<select class="border border-gray-300 px-3 py-2 rounded">
				<option>All Alerts</option>
				<option>Low Stock</option>
				<option>Out of Stock</option>
			</select>
			<select class="border border-gray-300 px-3 py-2 rounded">
				<option>All Categories</option>
				<option>Medications</option>
				<option>Medical Supplies</option>
			</select>
		</div>

		<!-- Tabs -->
		<div class="flex flex-wrap gap-2 mb-6 text-sm">
			<button class="px-3 py-1 bg-gray-900 text-white rounded">Low Stock</button>
			<button class="px-3 py-1 bg-gray-100 text-gray-700 rounded hover:bg-gray-200">
				Out of Stock
			</button>
			<button class="px-3 py-1 bg-gray-100 text-gray-700 rounded hover:bg-gray-200">
				Expiring Soon
			</button>
			<button class="px-3 py-1 bg-gray-100 text-gray-700 rounded hover:bg-gray-200">
				All Alerts
			</button>
		</div>

		<!-- Table -->
		<div class="bg-white border rounded shadow-sm">
			<div class="p-4 border-b text-sm text-gray-700 font-semibold">Low Stock Items</div>
			<p class="px-4 pt-1 text-sm text-gray-500 mb-2">
				Items that have fallen below their minimum stock level
			</p>
			<div class="overflow-auto">
				<table class="min-w-full text-sm text-left">
					<thead class="bg-gray-100 text-gray-600 uppercase">
						<tr>
							<th class="px-4 py-2">Item ID</th>
							<th class="px-4 py-2">Name</th>
							<th class="px-4 py-2">Category</th>
							<th class="px-4 py-2">Current Stock</th>
							<th class="px-4 py-2">Min. Level</th>
							<th class="px-4 py-2">Status</th>
							<th class="px-4 py-2">Supplier</th>
							<th class="px-4 py-2">Actions</th>
						</tr>
					</thead>
					<tbody>
						<tr
							v-for="item in lowStockItems"
							:key="item.id"
							class="border-b hover:bg-gray-50"
						>
							<td class="px-4 py-2 font-medium text-gray-800">{{ item.id }}</td>
							<td class="px-4 py-2">{{ item.name }}</td>
							<td class="px-4 py-2">{{ item.category }}</td>
							<td class="px-4 py-2">{{ item.stock }}</td>
							<td class="px-4 py-2">{{ item.min }}</td>
							<td class="px-4 py-2">
								<span
									class="bg-yellow-100 text-yellow-700 text-xs font-semibold px-2 py-1 rounded-full"
								>
									Low Stock
								</span>
							</td>
							<td class="px-4 py-2">{{ item.supplier }}</td>
							<td class="px-4 py-2">
								<span
									class="material-icons text-gray-500 cursor-pointer hover:text-gray-700"
									>more_vert</span
								>
							</td>
						</tr>
					</tbody>
				</table>
			</div>
		</div>
		<div class="mt-4">
			<div class="bg-white border rounded shadow-sm p-6">
				<h2 class="text-xl font-semibold">Alert Settings</h2>
				<p class="text-sm text-gray-500 mb-6">
					Configure how and when you receive inventory alerts
				</p>

				<div class="grid grid-cols-1 md:grid-cols-2 gap-4">
					<!-- Notification Preferences -->
					<div>
						<h3 class="text-sm font-medium text-gray-700 mb-2">
							Notification Preferences
						</h3>
						<div class="space-y-4">
							<div
								class="flex items-center justify-between border rounded px-4 py-3 bg-gray-50"
							>
								<div class="flex items-start gap-2">
									<span class="material-icons text-lg text-gray-500"
										>notifications</span
									>
									<div>
										<p class="text-sm font-medium text-gray-800">
											Email Notifications
										</p>
										<p class="text-xs text-gray-500">
											Receive alerts via email
										</p>
									</div>
								</div>
								<button class="text-sm text-blue-600 hover:underline">
									Configure
								</button>
							</div>

							<div
								class="flex items-center justify-between border rounded px-4 py-3 bg-gray-50"
							>
								<div class="flex items-start gap-2">
									<span class="material-icons text-lg text-gray-500"
										>schedule</span
									>
									<div>
										<p class="text-sm font-medium text-gray-800">
											Alert Frequency
										</p>
										<p class="text-xs text-gray-500">
											Daily summary at 9:00 AM
										</p>
									</div>
								</div>
								<button class="text-sm text-blue-600 hover:underline">
									Configure
								</button>
							</div>
						</div>
					</div>

					<!-- Alert Thresholds -->
					<div>
						<h3 class="text-sm font-medium text-gray-700 mb-2">Alert Thresholds</h3>
						<div class="space-y-4">
							<div
								class="flex items-center justify-between border rounded px-4 py-3 bg-gray-50"
							>
								<div class="flex items-start gap-2">
									<span class="material-icons text-lg text-yellow-500"
										>warning</span
									>
									<div>
										<p class="text-sm font-medium text-gray-800">
											Low Stock Threshold
										</p>
										<p class="text-xs text-gray-500">
											Default: 20% of minimum level
										</p>
									</div>
								</div>
								<button class="text-sm text-blue-600 hover:underline">
									Configure
								</button>
							</div>

							<div
								class="flex items-center justify-between border rounded px-4 py-3 bg-gray-50"
							>
								<div class="flex items-start gap-2">
									<span class="material-icons text-lg text-gray-500">event</span>
									<div>
										<p class="text-sm font-medium text-gray-800">
											Expiry Alert Period
										</p>
										<p class="text-xs text-gray-500">
											Default: 30 days before expiry
										</p>
									</div>
								</div>
								<button class="text-sm text-blue-600 hover:underline">
									Configure
								</button>
							</div>
						</div>
					</div>
				</div>
			</div>
		</div>
	</div>
</template>

<script setup>
const lowStockItems = [
	{
		id: 'INV002',
		name: 'Ibuprofen 200mg',
		category: 'Medications',
		stock: 12,
		min: 15,
		supplier: 'PharmaTech Inc.',
	},
	{
		id: 'INV005',
		name: 'Amoxicillin 500mg',
		category: 'Medications',
		stock: 8,
		min: 10,
		supplier: 'MedPlus Supplies',
	},
	{
		id: 'INV007',
		name: 'Examination Table Paper',
		category: 'Medical Supplies',
		stock: 3,
		min: 5,
		supplier: 'Health Supply Co.',
	},
	{
		id: 'INV011',
		name: 'Surgical Gloves (Medium)',
		category: 'Medical Supplies',
		stock: 45,
		min: 50,
		supplier: 'MedEquip Solutions',
	},
	{
		id: 'INV015',
		name: 'Bandages (Box)',
		category: 'Medical Supplies',
		stock: 7,
		min: 10,
		supplier: 'Health Supply Co.',
	},
	{
		id: 'INV018',
		name: 'Antiseptic Solution',
		category: 'Medical Supplies',
		stock: 4,
		min: 6,
		supplier: 'MedPlus Supplies',
	},
	{
		id: 'INV023',
		name: 'Syringes 10ml',
		category: 'Medical Supplies',
		stock: 30,
		min: 40,
		supplier: 'MedEquip Solutions',
	},
]
</script>

<style scoped>
@import url('https://fonts.googleapis.com/icon?family=Material+Icons');
</style>
